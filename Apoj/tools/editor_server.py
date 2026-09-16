# -*- coding: utf-8 -*-
import os
import json
import sys
import time
import re
import webbrowser
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))
ASSETS_AUDIO = os.path.join(PROJECT_ROOT, 'app', 'src', 'main', 'assets', 'audio')
ASSETS_CLIPS = os.path.join(PROJECT_ROOT, 'app', 'src', 'main', 'assets', 'clips')
REPO_AUDIO = os.path.abspath('C:/Projects My/Android_Repo/Apoj/audio')
REPO_CLIPS = os.path.abspath('C:/Projects My/Android_Repo/Apoj/clips')
DB_FILE = os.path.join(BASE_DIR, 'songs_db.json')
ASSETS_DB = os.path.join(PROJECT_ROOT, 'app', 'src', 'main', 'assets', 'songs_db.json')
REPO_DB = os.path.abspath('C:/Projects My/Android_Repo/Apoj/database/songs_db.json')

def find_available_port(start_port=38090, max_attempts=100):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

class ApojEditorHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def serve_file_with_range(self, file_path, content_type):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            self.send_response(404)
            self.end_headers()
            return

        file_size = os.path.getsize(file_path)
        range_header = self.headers.get('Range', None)

        if range_header:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else file_size - 1
                if start >= file_size:
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{file_size}')
                    self.end_headers()
                    return
                end = min(end, file_size - 1)
                chunk_len = end - start + 1

                self.send_response(206)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
                self.send_header('Content-Length', str(chunk_len))
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                with open(file_path, 'rb') as f:
                    f.seek(start)
                    self.wfile.write(f.read(chunk_len))
                return

        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(file_size))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open(file_path, 'rb') as f:
            shutil.copyfileobj(f, self.wfile)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/songs':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            if os.path.exists(DB_FILE):
                with open(DB_FILE, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'[]')

        elif path.startswith('/audio/'):
            raw_filename = urllib.parse.unquote(path[len('/audio/'):])
            base_name = os.path.splitext(raw_filename)[0]
            candidates = [
                os.path.join(ASSETS_AUDIO, f"{base_name}.wav"),
                os.path.join(REPO_AUDIO, f"{base_name}.wav"),
                os.path.join(ASSETS_AUDIO, f"{base_name}.mp3"),
                os.path.join(REPO_AUDIO, f"{base_name}.mp3"),
                os.path.join(ASSETS_AUDIO, raw_filename),
                os.path.join(REPO_AUDIO, raw_filename),
                os.path.join(BASE_DIR, 'audio', f"{base_name}.wav"),
                os.path.join(BASE_DIR, 'audio', raw_filename),
            ]
            found = None
            for c in candidates:
                if os.path.exists(c) and os.path.getsize(c) > 0:
                    found = c
                    break

            if found:
                mime = 'audio/wav' if found.endswith('.wav') else 'audio/mpeg'
                self.serve_file_with_range(found, mime)
            else:
                self.send_response(404)
                self.end_headers()

        elif path.startswith('/clips/'):
            raw_filename = urllib.parse.unquote(path[len('/clips/'):])
            base_name = os.path.splitext(raw_filename)[0]
            candidates = [
                os.path.join(ASSETS_CLIPS, f"{base_name}.mp4"),
                os.path.join(REPO_CLIPS, f"{base_name}.mp4"),
                os.path.join(ASSETS_CLIPS, raw_filename),
                os.path.join(REPO_CLIPS, raw_filename),
                os.path.join(BASE_DIR, 'clips', f"{base_name}.mp4"),
                os.path.join(BASE_DIR, 'clips', raw_filename),
            ]
            found = None
            for c in candidates:
                if os.path.exists(c) and os.path.getsize(c) > 0:
                    found = c
                    break

            if found:
                self.serve_file_with_range(found, 'video/mp4')
            else:
                self.send_response(404)
                self.end_headers()

        elif path == '/' or path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            index_path = os.path.join(BASE_DIR, 'index.html')
            with open(index_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            try:
                songs = json.loads(data.decode('utf-8'))
                # 1. Save to local tools DB
                with open(DB_FILE, 'w', encoding='utf-8') as f:
                    json.dump(songs, f, ensure_ascii=False, indent=2)

                # 2. Save to app assets
                os.makedirs(os.path.dirname(ASSETS_DB), exist_ok=True)
                with open(ASSETS_DB, 'w', encoding='utf-8') as f:
                    json.dump(songs, f, ensure_ascii=False, indent=2)

                # 3. Save to common repo DB
                os.makedirs(os.path.dirname(REPO_DB), exist_ok=True)
                with open(REPO_DB, 'w', encoding='utf-8') as f:
                    json.dump(songs, f, ensure_ascii=False, indent=2)

                response = {
                    "status": "success",
                    "message": "База песен успешно сохранена и синхронизирована!",
                    "totalSongs": len(songs)
                }
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                print(f"[ApojEditor] Saved {len(songs)} songs to local, assets, and repo DB.")
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "error": str(e)}).encode('utf-8'))

        elif parsed.path == '/api/sync':
            try:
                if os.path.exists(DB_FILE):
                    shutil.copy2(DB_FILE, ASSETS_DB)
                    os.makedirs(os.path.dirname(REPO_DB), exist_ok=True)
                    shutil.copy2(DB_FILE, REPO_DB)
                response = {"status": "success", "message": "Все файлы базы данных успешно синхронизированы!"}
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "error": str(e)}).encode('utf-8'))

        elif parsed.path == '/api/download_clip':
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            try:
                import imageio_ffmpeg
                import subprocess

                body = json.loads(data.decode('utf-8'))
                song_id = body.get('songId', 'song_' + str(int(time.time())))
                query_or_url = body.get('url', '').strip()
                start_time = float(body.get('startTime', 0.0))
                duration = float(body.get('duration', 15.0))

                if not query_or_url:
                    raise ValueError("Не указан URL или поисковый запрос YouTube.")

                ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
                temp_dir = os.path.join(BASE_DIR, 'temp_downloads')
                os.makedirs(temp_dir, exist_ok=True)
                temp_video = os.path.join(temp_dir, f"{song_id}_raw.mp4")

                target = query_or_url
                if not target.startswith('http://') and not target.startswith('https://'):
                    target = f"ytsearch1:{target}"

                print(f"[ApojEditor] Downloading video/audio from: {target} for song: {song_id}...")
                cmd_ytdlp = [
                    'yt-dlp',
                    '--format', 'bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    '--merge-output-format', 'mp4',
                    '-o', temp_video,
                    '--no-playlist',
                    '--force-overwrites',
                    target
                ]
                subprocess.run(cmd_ytdlp, check=True, timeout=120)

                # Process 15s HD video clip (720p, h264)
                target_clip_assets = os.path.join(ASSETS_CLIPS, f"{song_id}.mp4")
                target_clip_repo = os.path.join(REPO_CLIPS, f"{song_id}.mp4")
                os.makedirs(os.path.dirname(target_clip_assets), exist_ok=True)
                os.makedirs(os.path.dirname(target_clip_repo), exist_ok=True)

                cmd_clip = [
                    ffmpeg, '-y',
                    '-ss', str(start_time),
                    '-i', temp_video,
                    '-t', str(duration),
                    '-vf', 'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1',
                    '-c:v', 'libx264', '-preset', 'fast', '-crf', '22',
                    '-c:a', 'aac', '-b:a', '192k',
                    target_clip_assets
                ]
                subprocess.run(cmd_clip, check=True)
                if os.path.exists(os.path.dirname(target_clip_repo)):
                    shutil.copy2(target_clip_assets, target_clip_repo)

                # Process and normalize audio WAV (44.1kHz mono, -14 LUFS)
                target_audio_assets = os.path.join(ASSETS_AUDIO, f"{song_id}.wav")
                target_audio_repo = os.path.join(REPO_AUDIO, f"{song_id}.wav")
                os.makedirs(os.path.dirname(target_audio_assets), exist_ok=True)
                os.makedirs(os.path.dirname(target_audio_repo), exist_ok=True)

                cmd_audio = [
                    ffmpeg, '-y',
                    '-ss', str(start_time),
                    '-i', temp_video,
                    '-t', str(duration),
                    '-vn',
                    '-af', 'loudnorm=I=-14:LRA=11:TP=-1.5',
                    '-ac', '1',
                    '-ar', '44100',
                    target_audio_assets
                ]
                subprocess.run(cmd_audio, check=True)
                if os.path.exists(os.path.dirname(target_audio_repo)):
                    shutil.copy2(target_audio_assets, target_audio_repo)

                if os.path.exists(temp_video):
                    try: os.remove(temp_video)
                    except Exception: pass

                response = {
                    "status": "success",
                    "message": f"Видеоклип и аудио для '{song_id}' успешно скачаны и нормализованы!",
                    "clipUrl": f"/clips/{song_id}.mp4",
                    "audioUrl": f"/audio/{song_id}.wav",
                    "durationSec": duration
                }
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                print(f"[ApojEditor] Successfully downloaded & processed clip for {song_id}")
            except Exception as e:
                print(f"[ApojEditor] Error downloading clip: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "error": str(e)}).encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    port = find_available_port(start_port=38090)
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, ApojEditorHandler)
    url = f"http://localhost:{port}"
    print(f"============================================================")
    print(f" АПОЖ (SingItBack): Редактор каталога песен и викторины")
    print(f" Web UI Address: {url}")
    print(f" Открытие браузера...")
    print(f" Нажмите Ctrl+C для остановки сервера.")
    print(f"============================================================")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
