# -*- coding: utf-8 -*-
import json
import os
import sys

from cat_soviet import SOVIET_SONGS
from cat_rock import ROCK_SONGS
from cat_pop import POP_SONGS
from cat_kids import KIDS_SONGS
from cat_world import WORLD_SONGS
from cat_memes import MEMES_SONGS

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_songs = SOVIET_SONGS + ROCK_SONGS + POP_SONGS + KIDS_SONGS + WORLD_SONGS + MEMES_SONGS

print(f"Total songs collected: {len(all_songs)}")
print(f" - Soviet: {len(SOVIET_SONGS)}")
print(f" - Rock: {len(ROCK_SONGS)}")
print(f" - Pop: {len(POP_SONGS)}")
print(f" - Kids: {len(KIDS_SONGS)}")
print(f" - World: {len(WORLD_SONGS)}")
print(f" - Memes: {len(MEMES_SONGS)}")

# Validation checks
ids = set()
for s in all_songs:
    # 1. Unique ID
    assert s["id"] not in ids, f"Duplicate id: {s['id']}"
    ids.add(s["id"])
    
    # 2. Segments
    assert 3 <= len(s["segments"]) <= 6, f"Invalid segments count in {s['id']}"
    
    # 3. Options
    assert len(s["options"]) == 4, f"Options count must be 4 in {s['id']}"
    correct_count = sum(1 for o in s["options"] if o["isCorrect"])
    assert correct_count == 1, f"Must have exactly 1 correct option in {s['id']}, found {correct_count}"
    
    # 4. Melody Notes
    assert len(s["melodyNotes"]) >= 6, f"Melody notes must have at least 6 notes in {s['id']}"

print("All validation checks PASSED successfully!")

# Target paths
paths = [
    os.path.abspath("tools/songs_db.json"),
    os.path.abspath("app/src/main/assets/songs_db.json"),
    os.path.abspath("C:/Projects My/Android_Repo/Apoj/database/songs_db.json")
]

json_content = json.dumps(all_songs, ensure_ascii=False, indent=2)

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(json_content)
    print(f"Written database to: {p} ({len(all_songs)} songs, {len(json_content)} bytes)")

print("Database generation complete!")
