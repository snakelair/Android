# -*- coding: utf-8 -*-
import os
import sys
import glob
import json
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import imageio_ffmpeg
import yt_dlp

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

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

RETRY_QUERIES = {
    "soviet_prekrasnoe_daleko": {"query": "Прекрасное далеко песня Слышу голос", "start": 20},
    "pop_vse_chto_kasaetsya": {"query": "Звери Все что тебя касается клип", "start": 30},
    "kids_lvenok_cherepaha": {"query": "Я на солнышке лежу песня мультфильм", "start": 10},
    "kids_antoshka": {"query": "Антошка Антошка пойдем копать картошку", "start": 10},
    "kids_chunga_changa": {"query": "Чунга-Чанга синий небосвод Катерок", "start": 15},
    "kids_goluboy_vagon": {"query": "Голубой вагон бежит качается Шапокляк", "start": 15},
    "kids_krokodil_gena": {"query": "Пусть бегут неуклюже пешеходы по лужам песня", "start": 10},
    "kids_krasnaya_shapochka": {"query": "А-а в Африке реки вот такой ширины песня", "start": 15},
    "kids_oblaka_loshadki": {"query": "Облака белогривые лошадки песня Трям", "start": 15},
    "kids_ulybka": {"query": "От улыбки хмурый день светлей песня", "start": 15},
    "kids_spyat_ustalye_igrushki": {"query": "Спят усталые игрушки книжки спят песня", "start": 10},
    "kids_plastilinovaya_vorona": {"query": "Пластилиновая ворона мультфильм песня", "start": 15},
    "kids_babki_ezhki": {"query": "Растяни меха гармошка эх играй наяривай", "start": 10},
    "kids_vodyanoy": {"query": "Я Водяной я Водяной песня Папанов", "start": 10},
    "kids_fiksiki": {"query": "Кто такие фиксики большой секрет песня", "start": 10},
    "kids_ot_vinta": {"query": "От винта Смешарики песня клип", "start": 15},
    "memes_siniy_traktor": {"query": "Синий трактор По полям по полям", "start": 10}
}

def find_raw_file(track_id):
    pattern = os.path.join(TEMP_DIR, f"{track_id}_retry*")
    matches = glob.glob(pattern)
    for m in matches:
        if os.path.exists(m) and os.path.getsize(m) > 100000:
            return m
    return None

def process_retry_item(item):
    track_id, info = item
    query = info["query"]
    start_sec = info["start"]
    duration = 15.0

    clip_out = os.path.join(ASSETS_CLIPS, f"{track_id}.mp4")
    audio_out = os.path.join(ASSETS_AUDIO, f"{track_id}.wav")
    repo_clip_out = os.path.join(REPO_CLIPS, f"{track_id}.mp4")
    repo_audio_out = os.path.join(REPO_AUDIO, f"{track_id}.wav")

    out_tmpl = os.path.join(TEMP_DIR, f"{track_id}_retry.%(ext)s")
    search_query = f"ytsearch5:{query}"
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
            ydl.download([search_query])
    except Exception as e:
        pass

    raw_file = find_raw_file(track_id)
    if not raw_file:
        return track_id, False, "not found on retry"

    # Process clip
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

    # Process audio
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

    if (os.path.exists(clip_out) and os.path.getsize(clip_out) > 50000 and
        os.path.exists(audio_out) and os.path.getsize(audio_out) > 50000):
        shutil.copy2(clip_out, repo_clip_out)
        shutil.copy2(audio_out, repo_audio_out)
        return track_id, True, "success"

    return track_id, False, "failed to process"

def main():
    print(f"Retrying {len(RETRY_QUERIES)} songs...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_retry_item, it) for it in RETRY_QUERIES.items()]
        for f in as_completed(futures):
            tid, ok, msg = f.result()
            print(f"[{'OK' if ok else 'FAIL'}] {tid}: {msg}")

if __name__ == "__main__":
    main()
