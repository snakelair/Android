# -*- coding: utf-8 -*-
import os
import json
import sys
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
