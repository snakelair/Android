# -*- coding: utf-8 -*-
import os
import sys
import glob
import json
import subprocess
import imageio_ffmpeg
import yt_dlp
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
FFMPEG_DIR = os.path.dirname(FFMPEG_EXE)
os.environ["PATH"] = FFMPEG_DIR + os.pathsep + os.environ.get("PATH", "")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
ASSETS_AUDIO = os.path.join(PROJECT_ROOT, "app", "src", "main", "assets", "audio")
ASSETS_CLIPS = os.path.join(PROJECT_ROOT, "app", "src", "main", "assets", "clips")
REPO_AUDIO = os.path.abspath("C:/Projects My/Android_Repo/Apoj/audio")
REPO_CLIPS = os.path.abspath("C:/Projects My/Android_Repo/Apoj/clips")
TEMP_DIR = os.path.join(BASE_DIR, "temp_downloads")
DB_FILE = os.path.join(BASE_DIR, "songs_db.json")

os.makedirs(ASSETS_AUDIO, exist_ok=True)
os.makedirs(ASSETS_CLIPS, exist_ok=True)
os.makedirs(REPO_AUDIO, exist_ok=True)
os.makedirs(REPO_CLIPS, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

def load_catalog():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def find_raw_file(track_id):
    pattern = os.path.join(TEMP_DIR, f"{track_id}_raw*")
    matches = glob.glob(pattern)
    for m in matches:
        if os.path.getsize(m) > 100000:
            return m
    return None

def process_song(song, force=False):
    track_id = song["id"]
    title = song["title"]
    artist = song["artist"]
    query = f"{artist} {title}"
    start_sec = 15.0
    duration = song.get("durationSec", 15.0)

    clip_out = os.path.join(ASSETS_CLIPS, f"{track_id}.mp4")
    audio_out = os.path.join(ASSETS_AUDIO, f"{track_id}.wav")
    repo_clip_out = os.path.join(REPO_CLIPS, f"{track_id}.mp4")
    repo_audio_out = os.path.join(REPO_AUDIO, f"{track_id}.wav")

    if not force and os.path.exists(clip_out) and os.path.exists(audio_out):
        print(f"[EXISTS] {track_id} already prepared.")
        return

    raw_file = find_raw_file(track_id)

    if not raw_file:
        print(f"\n[DOWNLOAD] {track_id}: {query}")
        out_template = os.path.join(TEMP_DIR, f"{track_id}_raw.%(ext)s")
        search_query = f"ytsearch5:{query}"
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
            'outtmpl': out_template,
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
            'max_downloads': 1,
            'ignoreerrors': True
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([search_query])
        except Exception as e:
            print(f"Error downloading {track_id}: {e}")

        raw_file = find_raw_file(track_id)

    if not raw_file:
        print(f"[ERROR] Could not find raw file for {track_id}")
        return

    print(f"[FFMPEG] Cutting & Normalizing {track_id} from {raw_file}...")

    # 1. Video Clip MP4 (720p, Normalized Audio -14 LUFS)
    cmd_clip = [
        FFMPEG_EXE, "-y",
        "-ss", str(start_sec),
        "-t", str(duration),
        "-i", raw_file,
        "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
        "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
        "-c:a", "aac", "-b:a", "128k",
        clip_out
    ]
    subprocess.run(cmd_clip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 2. 16-bit 44.1kHz Mono WAV (for Audio Engine slicing & reversing)
    cmd_audio = [
        FFMPEG_EXE, "-y",
        "-ss", str(start_sec),
        "-t", str(duration),
        "-i", raw_file,
        "-vn",
        "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "1",
        audio_out
    ]
    subprocess.run(cmd_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Copy to common repository
    if os.path.exists(clip_out):
        shutil.copy2(clip_out, repo_clip_out)
    if os.path.exists(audio_out):
        shutil.copy2(audio_out, repo_audio_out)

    clip_size = os.path.getsize(clip_out) if os.path.exists(clip_out) else 0
    audio_size = os.path.getsize(audio_out) if os.path.exists(audio_out) else 0
    print(f"[OK] Finished {track_id}: clip={clip_size/1024:.0f} KB, audio={audio_size/1024:.0f} KB")

def main():
    songs = load_catalog()
    print(f"Loaded {len(songs)} songs from {DB_FILE}")
    if len(sys.argv) > 1 and sys.argv[1] != "--all":
        target_ids = sys.argv[1:]
        songs = [s for s in songs if s["id"] in target_ids]

    for idx, s in enumerate(songs, 1):
        print(f"\n--- [{idx}/{len(songs)}] {s['title']} ({s['artist']}) ---")
        try:
            process_song(s)
        except Exception as e:
            print(f"Error on {s['id']}: {e}")

    print("\n[COMPLETE] All processing completed!")

if __name__ == "__main__":
    main()
