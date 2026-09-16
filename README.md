# 🤖 Android Projects Hub — SnakeLair

Единый репозиторий для релизов, дистрибутивов APK и документации проектов для **Android TV, Google TV и Android Mobile**.

---

## 📱 Каталог проектов

| Проект | Описание | Версия | Платформа | Релиз (APK) |
| :--- | :--- | :---: | :---: | :---: |
| [🎤 **АПОЖ (Песня наоборот / SingItBack)**](./Apoj) | Музыкальная игра-викторина с реверсивным воспроизведением, выравниванием по нотам и спариванием со смартфоном | **v1.0.0** | Android TV / Google TV / Смартфоны | [Скачать APK (62.9 MB)](./Apoj/releases/Apoj-v1.0.0-release.apk) |
| [🎬 **Стоп-Кадр (StopFrame)**](./StopFrame) | Кино-викторина на память и внимательность для всей семьи | **v1.1.0** | Android TV / Google TV / Планшеты | [Скачать APK (14 MB)](./StopFrame/releases/StopFrame-v1.0.0-release.apk) |
| [🎵 **Tracker Music PRO**](./TrackerMusic) | Плеер трекерной музыки демосцены и кейгенов (WASM + 3D WebGL + Auto-Update + MediaSession + Deep Links) | **v1.0.2** | Android TV / Google TV / Планшеты / Смартфоны / Авто | [Скачать APK (2.75 MB)](./TrackerMusic/releases/TrackerMusic-v1.0.2-release.apk) |

---

## 📁 Структура репозитория

```text
Android/
├── README.md                      # Главный каталог проектов и руководство
├── Apoj/                          # Проект 1: АПОЖ (Android TV & Mobile)
│   ├── README.md                  # Полная документация, правила, архитектура
│   ├── database/                  # База каталога песен и фрагментов (songs_db.json)
│   ├── audio/                     # 16-bit 44.1kHz моно WAV треки
│   ├── clips/                     # 720p MP4 видеоклипы с нормализацией -14 LUFS
│   └── releases/                  # Подписанный Release APK
│       └── Apoj-v1.0.0-release.apk
├── StopFrame/                     # Проект 2: Стоп-Кадр (Android TV)
│   ├── README.md                  # Полная документация, скриншоты, правила
│   ├── releases/                  # Подписанные Release APK
│   │   └── StopFrame-v1.0.0-release.apk
│   └── screenshots/               # Скриншоты интерфейса и геймплея
└── TrackerMusic/                  # Проект 3: Tracker Music PRO (Android & Android TV)
    ├── README.md                  # Документация, QR-код, управление пультом TV & Bluetooth
    ├── update.json                # Манифест системы автообновления
    ├── releases/                  # Подписанные Release APK
    │   ├── TrackerMusic-v1.0.0-release.apk
    │   ├── TrackerMusic-v1.0.1-release.apk
    │   └── TrackerMusic-v1.0.2-release.apk
    └── screenshots/               # TV баннер, QR-код для установки и скриншоты TV
```
