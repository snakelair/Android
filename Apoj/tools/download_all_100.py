# -*- coding: utf-8 -*-
import os
import sys
import glob
import json
import time
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
DB_FILE = os.path.join(BASE_DIR, "songs_db.json")

os.makedirs(ASSETS_AUDIO, exist_ok=True)
os.makedirs(ASSETS_CLIPS, exist_ok=True)
os.makedirs(REPO_AUDIO, exist_ok=True)
os.makedirs(REPO_CLIPS, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Custom search queries & start timestamps for accurate chorus/verse capture
TRACK_CONFIG = {
    # Soviet
    "soviet_pesenka_o_medvedyah": {"query": "Где то на белом свете песня Кавказская пленница", "start": 10},
    "soviet_ostrov_nevezeniya": {"query": "Остров невезения песня Миронов Бриллиантовая рука", "start": 12},
    "soviet_razgovor_so_schastyem": {"query": "Вдруг как в сказке скрипнула дверь Иван Васильевич", "start": 15},
    "soviet_pesnya_pro_zaytsev": {"query": "А нам все равно песня Никулин Бриллиантовая рука", "start": 15},
    "soviet_postoy_parovoz": {"query": "Постой паровоз песня Никулин Операция Ы", "start": 10},
    "soviet_prekrasnoe_daleko": {"query": "Прекрасное далеко песня Гостья из будущего", "start": 20},
    "soviet_krylatye_kacheli": {"query": "Крылатые качели Приключения Электроника", "start": 15},
    "soviet_est_tolko_mig": {"query": "Есть только миг Олег Анофриев Земля Санникова", "start": 15},
    "soviet_nadezhda": {"query": "Надежда мой компас земной Анна Герман", "start": 20},
    "soviet_trava_u_doma": {"query": "Земляне Трава у дома Земля в иллюминаторе", "start": 30},
    "soviet_siniy_iney": {"query": "Поющие гитары Синий синий иней лег на провода", "start": 15},
    "soviet_million_alyh_roz": {"query": "Алла Пугачева Миллион алых роз", "start": 60},
    "soviet_komarovo": {"query": "Игорь Скляр Комарово на недельку до второго", "start": 25},
    "soviet_deltaplan": {"query": "Валерий Леонтьев Полет на дельтаплане", "start": 35},
    "soviet_zelenoglazoe_taksi": {"query": "Михаил Боярский Зеленоглазое такси", "start": 25},
    "soviet_gardemariny": {"query": "Не вешать нос гардемарины песня Харатьян", "start": 15},
    "soviet_tri_belyh_konya": {"query": "Три белых коня Чародеи Лариса Долина", "start": 20},
    "soviet_vashe_blagorodie": {"query": "Ваше благородие госпожа удача Луспекаев", "start": 10},
    "soviet_temnaya_noch": {"query": "Темная ночь Марк Бернес", "start": 15},
    "soviet_shpaga": {"query": "Песня о шпаге Андрей Миронов Вжик вжик", "start": 10},

    # Rock
    "rock_gruppa_krovi": {"query": "Кино Группа крови", "start": 40},
    "rock_batareyka": {"query": "Жуки Батарейка О-о-и-я-и-ё", "start": 18},
    "rock_lesnik": {"query": "Король и Шут Лесник Будь как дома путник", "start": 30},
    "rock_zvezda_solntse": {"query": "Кино Звезда по имени Солнце Белый снег", "start": 25},
    "rock_prygnu_so_skaly": {"query": "Король и Шут Прыгну со скалы", "start": 45},
    "rock_polkovniku": {"query": "Би-2 Полковнику никто не пишет", "start": 40},
    "rock_varvara": {"query": "Би-2 Варвара Порвали паруса", "start": 35},
    "rock_moe_serdtse": {"query": "Сплин Мое сердце остановилось", "start": 40},
    "rock_vyhoda_net": {"query": "Сплин Выхода нет Скоро рассвет", "start": 35},
    "rock_skazochnaya_tayga": {"query": "Агата Кристи Сказочная тайга", "start": 35},
    "rock_kak_na_voyne": {"query": "Агата Кристи Как на войне Я беру портвейн", "start": 30},
    "rock_chto_takoe_osen": {"query": "ДДТ Что такое осень это небо", "start": 35},
    "rock_bespechny_angel": {"query": "Ария Беспечный ангел Этот парень был из тех", "start": 40},
    "rock_ulitsa_roz": {"query": "Ария Улица Роз Жанна из тех королев", "start": 45},
    "rock_vladivostok_2000": {"query": "Мумий Тролль Владивосток 2000 Уходим", "start": 30},
    "rock_skovannye": {"query": "Наутилус Помпилиус Скованные одной цепью", "start": 35},
    "rock_tulula": {"query": "Чичерина Ту-лу-ла В голове моей замкнуло", "start": 30},
    "rock_iskala": {"query": "Земфира Я искала тебя ночами темными", "start": 35},
    "rock_hali_gali": {"query": "Леприконсы Хали-гали паратрупер", "start": 25},
    "rock_kamorka": {"query": "Чиж и Ко О любви А не спеть ли мне песню", "start": 15},

    # Pop
    "pop_sedaya_noch": {"query": "Юрий Шатунов Седая ночь", "start": 65},
    "pop_topoliny_puh": {"query": "Иванушки International Тополиный пух", "start": 48},
    "pop_znaesh_li_ty": {"query": "МакSим Знаешь ли ты вдоль ночных дорог", "start": 62},
    "pop_18_mne_uzhe": {"query": "Руки Вверх 18 мне уже Забирай меня скорей", "start": 35},
    "pop_kroshka_moya": {"query": "Руки Вверх Крошка моя я по тебе скучаю", "start": 30},
    "pop_belye_rozy": {"query": "Ласковый май Белые розы", "start": 40},
    "pop_tuchi": {"query": "Иванушки International Тучи А тучи как люди", "start": 35},
    "pop_rayony_kvartaly": {"query": "Звери Районы кварталы жилые массивы", "start": 35},
    "pop_vse_chto_kasaetsya": {"query": "Звери Все что тебя касается", "start": 30},
    "pop_lyubi_menya_lyubi": {"query": "Отпетые Мошенники Люби меня люби", "start": 35},
    "pop_devushki_kak_zvezdy": {"query": "Андрей Губин Такие девушки как звезды", "start": 35},
    "pop_zima_holoda": {"query": "Андрей Губин Зима холода одинокие дома", "start": 30},
    "pop_samba_motylka": {"query": "Валерий Меладзе Самба белого мотылька", "start": 35},
    "pop_tekila_lyubov": {"query": "Валерий Меладзе Текила любовь", "start": 30},
    "pop_tsvet_nastroeniya": {"query": "Филипп Киркоров Цвет настроения синий", "start": 40},
    "pop_kon_lyube": {"query": "Любэ Выйду ночью в поле с конем", "start": 20},
    "pop_ty_uznaesh_ee": {"query": "Корни Ты узнаешь ее из тысячи", "start": 35},
    "pop_glukoza_nevesta": {"query": "Глюкоза Я буду вместо нее твоя невеста", "start": 30},
    "pop_tsaritsa_asti": {"query": "ANNA ASTI Царица Мальчик поплыл", "start": 45},
    "pop_spektakl_okonchen": {"query": "Полина Гагарина Спектакль окончен", "start": 40},

    # Kids
    "kids_mamontenok": {"query": "Песенка мамонтенка плыву я на белом", "start": 10},
    "kids_bremenskie": {"query": "Бременские музыканты Ничего на свете лучше нету", "start": 10},
    "kids_luch_solntsa": {"query": "Луч солнца золотого Магомаев Бременские музыканты", "start": 15},
    "kids_lvenok_cherepaha": {"query": "Я на солнышке лежу Львенок и черепаха песня", "start": 10},
    "kids_antoshka": {"query": "Антошка пойдем копать картошку мультфильм", "start": 10},
    "kids_chunga_changa": {"query": "Чунга Чанга синий небосвод мультфильм", "start": 15},
    "kids_goluboy_vagon": {"query": "Голубой вагон бежит качается мультфильм", "start": 15},
    "kids_krokodil_gena": {"query": "Пусть бегут неуклюже пешеходы по лужам", "start": 10},
    "kids_buratino": {"query": "Буратино песня Скажите как его зовут", "start": 15},
    "kids_krasnaya_shapochka": {"query": "Песня Красной Шапочки А-а в Африке реки", "start": 15},
    "kids_oblaka_loshadki": {"query": "Облака белогривые лошадки мультфильм", "start": 15},
    "kids_kuznechik": {"query": "В траве сидел кузнечик мультфильм Незнайка", "start": 10},
    "kids_ulybka": {"query": "От улыбки хмурый день светлей Крошка Енот", "start": 15},
    "kids_kaby_ne_bylo_zimy": {"query": "Кабы не было зимы Простоквашино Толкунова", "start": 10},
    "kids_spyat_ustalye_igrushki": {"query": "Спят усталые игрушки Спокойной ночи малыши", "start": 10},
    "kids_plastilinovaya_vorona": {"query": "Пластилиновая ворона мультфильм песня", "start": 15},
    "kids_babki_ezhki": {"query": "Частушки Бабок Ежек Летучий корабль", "start": 10},
    "kids_vodyanoy": {"query": "Я водяной я водяной Летучий корабль", "start": 10},
    "kids_fiksiki": {"query": "А кто такие фиксики большой секрет", "start": 10},
    "kids_ot_vinta": {"query": "От винта Смешарики песня", "start": 15},

    # World
    "world_queen_bohemian_rhapsody": {"query": "Queen Bohemian Rhapsody official video", "start": 50},
    "world_queen_we_will_rock_you": {"query": "Queen We Will Rock You official", "start": 10},
    "world_imagine_dragons_believer": {"query": "Imagine Dragons Believer official", "start": 35},
    "world_michael_jackson_billie_jean": {"query": "Michael Jackson Billie Jean official video", "start": 55},
    "world_beatles_yesterday": {"query": "The Beatles Yesterday live official", "start": 10},
    "world_beatles_yellow_submarine": {"query": "The Beatles Yellow Submarine official", "start": 15},
    "world_abba_dancing_queen": {"query": "ABBA Dancing Queen official video", "start": 20},
    "world_bon_jovi_its_my_life": {"query": "Bon Jovi It's My Life official music video", "start": 35},
    "world_nirvana_smells_like_teen_spirit": {"query": "Nirvana Smells Like Teen Spirit official music video", "start": 35},
    "world_acdc_highway_to_hell": {"query": "AC/DC Highway to Hell official video", "start": 30},
    "world_linkin_park_in_the_end": {"query": "Linkin Park In the End official music video", "start": 40},
    "world_coldplay_viva_la_vida": {"query": "Coldplay Viva La Vida official video", "start": 30},
    "world_aha_take_on_me": {"query": "a-ha Take On Me official video", "start": 40},
    "world_adele_rolling_in_the_deep": {"query": "Adele Rolling in the Deep official video", "start": 35},
    "world_survivor_eye_of_the_tiger": {"query": "Survivor Eye of the Tiger official video", "start": 40},
    "world_eagles_hotel_california": {"query": "Eagles Hotel California live 1977", "start": 50},
    "world_george_michael_careless_whisper": {"query": "George Michael Careless Whisper official video", "start": 40},
    "world_ed_sheeran_shape_of_you": {"query": "Ed Sheeran Shape of You official music video", "start": 30},

    # Memes
    "memes_yagoda_malinka": {"query": "Хабиб Ягода малинка оп-оп-оп", "start": 45},
    "memes_matushka_zemlya": {"query": "Матушка Земля белая березонька Куртукова", "start": 45},
    "memes_skibidi": {"query": "Little Big Skibidi romantic edition", "start": 25},
    "memes_uno": {"query": "Little Big UNO Eurovision official video", "start": 30},
    "memes_venera_yupiter": {"query": "Ваня Дмитриенко Венера-Юпитер клип", "start": 35},
    "memes_lyubimka": {"query": "NILETTO Любимка клип Время пострелять", "start": 30},
    "memes_malinovy_zakat": {"query": "Макс Корж Малиновый закат", "start": 35},
    "memes_siniy_traktor": {"query": "Синий трактор По полям по полям едет к нам", "start": 10},
    "memes_po_baram": {"query": "ANNA ASTI По барам клип", "start": 45},
    "memes_malchik_na_devyatke": {"query": "DEAD BLONDE Мальчик на девятке клип", "start": 30},
    "memes_gangnam_style": {"query": "PSY Gangnam Style official music video", "start": 40},
    "memes_crazy_frog": {"query": "Crazy Frog Axel F official video", "start": 25},
    "memes_plachu_na_tehno": {"query": "Cream Soda Хлеб Плачу на техно клип", "start": 30},
    "memes_ugonschitsa": {"query": "Ирина Аллегрова Угонщица Угнала тебя", "start": 35},
    "memes_dip_haus": {"query": "Gayazovs Brothers Увезите меня на Дип-хаус", "start": 30},
    "memes_chastushki_sektor": {"query": "Сектор Газа Частушки Эх гармошка заиграла", "start": 15},
    "memes_dymok": {"query": "Ицык Цыпер Дымок пошел по комнате", "start": 20}
}

def find_raw_file(track_id):
    pattern = os.path.join(TEMP_DIR, f"{track_id}_raw*")
    matches = glob.glob(pattern)
    for m in matches:
        if os.path.exists(m) and os.path.getsize(m) > 100000:
            return m
    return None

def download_and_process_song(song):
    track_id = song["id"]
    duration = song.get("durationSec", 15.0)

    cfg = TRACK_CONFIG.get(track_id, {
        "query": f"{song['artist']} {song['title']}",
        "start": 25
    })
    query = cfg["query"]
    start_sec = cfg["start"]

    clip_out = os.path.join(ASSETS_CLIPS, f"{track_id}.mp4")
    audio_out = os.path.join(ASSETS_AUDIO, f"{track_id}.wav")
    repo_clip_out = os.path.join(REPO_CLIPS, f"{track_id}.mp4")
    repo_audio_out = os.path.join(REPO_AUDIO, f"{track_id}.wav")

    # Check if already processed
    if (os.path.exists(clip_out) and os.path.getsize(clip_out) > 50000 and
        os.path.exists(audio_out) and os.path.getsize(audio_out) > 50000):
        # ensure synced to repo
        if not os.path.exists(repo_clip_out):
            shutil.copy2(clip_out, repo_clip_out)
        if not os.path.exists(repo_audio_out):
            shutil.copy2(audio_out, repo_audio_out)
        return track_id, True, "already present"

    # Step 1: Download raw
    raw_file = find_raw_file(track_id)
    if not raw_file:
        out_tmpl = os.path.join(TEMP_DIR, f"{track_id}_raw.%(ext)s")
        search_query = f"ytsearch1:{query}"
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
            'outtmpl': out_tmpl,
            'ffmpeg_location': FFMPEG_DIR,
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
            'max_downloads': 1
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(search_query, download=True)
        except yt_dlp.utils.MaxDownloadsReached:
            pass
        except Exception as e:
            pass
        raw_file = find_raw_file(track_id)

    if not raw_file:
        return track_id, False, "download failed"

    # Step 2: Cut & Loudnorm Video Clip
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

    # Step 3: Cut & Loudnorm 44.1kHz mono WAV
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
        return track_id, True, "processed successfully"

    return track_id, False, "processing output missing"

def main():
    if not os.path.exists(DB_FILE):
        print("Database not found!")
        return

    with open(DB_FILE, "r", encoding="utf-8") as f:
        songs = json.load(f)

    total = len(songs)
    print(f"Starting concurrent download and processing for {total} songs...")

    successes = set()
    failures = set()

    max_workers = 4
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(download_and_process_song, s): s for s in songs}
        for future in as_completed(future_map):
            song = future_map[future]
            try:
                track_id, ok, msg = future.result()
                if ok:
                    successes.add(track_id)
                    print(f"[OK] ({len(successes)}/{total}) {track_id} -> {msg}")
                else:
                    failures.add(track_id)
                    print(f"[FAIL] ({len(failures)} failed) {track_id} -> {msg}")
            except Exception as e:
                failures.add(song["id"])
                print(f"[ERROR] {song['id']} -> {e}")

    print(f"\n==========================================")
    print(f"Completed download run: {len(successes)} succeeded, {len(failures)} failed.")

    # Filter catalog: Keep ONLY songs with verified audio & clips!
    verified_songs = []
    for s in songs:
        c_path = os.path.join(ASSETS_CLIPS, f"{s['id']}.mp4")
        a_path = os.path.join(ASSETS_AUDIO, f"{s['id']}.wav")
        if (os.path.exists(c_path) and os.path.getsize(c_path) > 50000 and
            os.path.exists(a_path) and os.path.getsize(a_path) > 50000):
            verified_songs.append(s)

    print(f"Verified 100% real songs with clips & audio: {len(verified_songs)}")

    # Update all 3 databases
    paths = [
        os.path.abspath("tools/songs_db.json"),
        os.path.abspath("app/src/main/assets/songs_db.json"),
        os.path.abspath("C:/Projects My/Android_Repo/Apoj/database/songs_db.json")
    ]
    json_str = json.dumps(verified_songs, ensure_ascii=False, indent=2)
    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(json_str)

    print("Databases updated with verified real songs only!")

if __name__ == "__main__":
    main()
