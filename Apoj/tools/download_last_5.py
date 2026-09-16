# -*- coding: utf-8 -*-
import os, sys, glob, shutil, subprocess
import imageio_ffmpeg, yt_dlp

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

ITEMS = [
    ("kids_lvenok_cherepaha", "Я на солнышке лежу песенка", 10),
    ("kids_antoshka", "Антошка Антошка Веселая карусель", 10),
    ("kids_chunga_changa", "Чунга Чанга синий небосвод Катерок", 15),
    ("kids_fiksiki", "Кто такие фиксики большой большой секрет", 10),
    ("memes_siniy_traktor", "По полям синий трактор едет к нам", 10)
]

for track_id, q, start_sec in ITEMS:
    clip_out = os.path.join(ASSETS_CLIPS, f"{track_id}.mp4")
    audio_out = os.path.join(ASSETS_AUDIO, f"{track_id}.wav")
    repo_clip = os.path.join(REPO_CLIPS, f"{track_id}.mp4")
    repo_audio = os.path.join(REPO_AUDIO, f"{track_id}.wav")

    out_tmpl = os.path.join(TEMP_DIR, f"{track_id}_final.%(ext)s")
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
        'outtmpl': out_tmpl,
        'ffmpeg_location': FFMPEG_DIR,
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'ignoreerrors': True,
        'max_downloads': 1
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch3:{q}"])
    except Exception as e:
        pass

    matches = glob.glob(os.path.join(TEMP_DIR, f"{track_id}_final*"))
    raw_file = None
    for m in matches:
        if os.path.exists(m) and os.path.getsize(m) > 100000:
            raw_file = m
            break

    if raw_file:
        # Process
        subprocess.run([
            FFMPEG_EXE, "-y", "-ss", str(start_sec), "-t", "15.0", "-i", raw_file,
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
            "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
            "-c:a", "aac", "-b:a", "128k", clip_out
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        subprocess.run([
            FFMPEG_EXE, "-y", "-ss", str(start_sec), "-t", "15.0", "-i", raw_file,
            "-vn", "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
            "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1", audio_out
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if os.path.exists(clip_out) and os.path.exists(audio_out):
            shutil.copy2(clip_out, repo_clip)
            shutil.copy2(audio_out, repo_audio)
            print(f"[OK] {track_id} downloaded and processed!")
        else:
            print(f"[FAIL] {track_id} processing failed")
    else:
        print(f"[FAIL] {track_id} raw download failed")
