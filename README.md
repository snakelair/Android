# 🤖 Android Projects Hub & Media CDN — SnakeLair

Единый репозиторий для релизов, дистрибутивов APK, документации и облачного медиа-хостинга проектов для **Android TV, Google TV и Android Mobile**.

---

## 📱 Каталог проектов

| Проект | Описание | Версия | Платформа | Релиз (APK) | Медиа / Хостинг |
| :--- | :--- | :---: | :---: | :---: | :---: |
| [🎬 **Стоп-Кадр (StopFrame)**](./StopFrame) | Кино-викторина на память и внимательность для всей семьи | **v1.0.0** | Android TV / Google TV / Планшеты | [Скачать APK (14 MB)](./StopFrame/releases/StopFrame-v1.0.0-release.apk) | [Видео-хостинг (13 отрывков)](./StopFrame/videos) |
| [🎵 **Tracker Music PRO**](./TrackerMusic) | Плеер трекерной музыки демосцены и кейгенов (WASM + 3D WebGL) | **v1.0.0** | Android TV / Google TV / Планшеты / Смартфоны | [Скачать APK (2.7 MB)](./TrackerMusic/releases/TrackerMusic-v1.0.0-release.apk) | [Веб-плеер 1,280+ треков](https://tracker.snakelair.ru/) |

---

## 📂 Структура репозитория

```text
Android/
├── README.md                      # Главный каталог проектов и руководство
├── StopFrame/                     # Проект 1: Стоп-Кадр (Android TV)
│   ├── README.md                  # Полная документация, скриншоты, правила
│   ├── releases/                  # Подписанные Release APK
│   │   └── StopFrame-v1.0.0-release.apk
│   ├── screenshots/               # Скриншоты интерфейса и геймплея
│   └── videos/                    # 1080p H.264 видеоклипы для прямого стриминга
└── TrackerMusic/                  # Проект 2: Tracker Music PRO (Android & Android TV)
    ├── README.md                  # Документация, QR-код, управление пультом TV
    ├── releases/                  # Подписанные Release APK
    │   └── TrackerMusic-v1.0.0-release.apk
    └── screenshots/               # TV баннер и QR-код для установки
```

---

## 🌐 Использование в качестве бесплатного медиа-CDN

Репозиторий используется как высокоскоростной медиа-хостинг для прямого воспроизведения в **Media3 ExoPlayer** без необходимости раздувать размер установочного APK.

* **Прямой URL для стриминга видео:**
  ```text
  https://raw.githubusercontent.com/snakelair/Android/main/<ProjectName>/videos/<video_name>.mp4
  ```
* **Преимущества:**
  - Поддержка заголовков `Range: bytes` для мгновенной буферизации и перемотки.
  - Высокая скорость через глобальный CDN GitHub / Fastly.
  - APK остается легковесным (всего ~14 МБ вместо 100+ МБ).

---

## 🛠️ Добавление новых проектов

Для добавления нового проекта в хаб:
1. Создайте отдельную директорию: `<ProjectName>/`.
2. Поместите подписанный APK в `<ProjectName>/releases/`.
3. Добавьте медиафайлы или ассеты в `<ProjectName>/media/` или `<ProjectName>/videos/`.
4. Создайте `<ProjectName>/README.md` с описанием приложения, скриншотами и инструкцией.
5. Зарегистрируйте проект в таблице выше.
