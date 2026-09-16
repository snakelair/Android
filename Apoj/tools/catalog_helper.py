# -*- coding: utf-8 -*-
def make_song(id, title, artist, category, year, durationSec, melodyNotes, segments_text, options_text, difficulty="EASY"):
    part_dur = durationSec / len(segments_text)
    segments = []
    for idx, (lbl, lyr) in enumerate(segments_text):
        segments.append({
            "id": idx + 1,
            "startSec": round(idx * part_dur, 2),
            "endSec": round((idx + 1) * part_dur, 2),
            "label": f"Часть {idx+1}: {lbl}",
            "lyricsSnippet": lyr
        })
    options = []
    for idx, (txt, is_corr) in enumerate(options_text):
        options.append({
            "id": idx + 1,
            "text": txt,
            "isCorrect": is_corr
        })
    return {
        "id": id,
        "title": title,
        "artist": artist,
        "category": category,
        "year": str(year),
        "durationSec": durationSec,
        "audioUrl": f"https://raw.githubusercontent.com/snakelair/SingItBack/main/audio/{id}.mp3",
        "clipUrl": f"https://raw.githubusercontent.com/snakelair/SingItBack/main/clips/{id}.mp4",
        "youtubeVideoId": id,
        "difficulty": difficulty,
        "isApproved": True,
        "melodyNotes": melodyNotes,
        "segments": segments,
        "options": options
    }
