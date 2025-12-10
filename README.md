# 🤖 Telegram Bot — Modular Command Handler

## 🧩 Overview
Project ini adalah **Telegram Bot modular** berbasis Python yang dirancang untuk dapat berkembang dengan mudah.  
Bot ini menggunakan library `python-telegram-bot` versi terbaru dan mendukung `async/await` sehingga performanya ringan dan responsif.

Struktur bot disiapkan agar **command baru dapat ditambahkan dengan cepat dan rapi**, sehingga cocok untuk:
- Bot internal tim
- Bot respon cepat
- Bot operasional yang berkembang secara bertahap
- Fondasi bot otomatis (Set Chat, Admin Tools, Workflow Bot, dsb.)

---

## 🚀 Fitur Saat Ini
Bot saat ini telah memiliki beberapa fungsi dasar dan siap menerima penambahan fitur baru.

### ✔️ Command yang tersedia
- `/salah`  
  Mengirimkan teks standar untuk keperluan respons cepat:
Siap mohon izin kami pedomani dan laksanakan mohon izin

### ✔️ Fondasi bot siap untuk:
- Menambah command baru
- Menambah inline button & callback
- Menambahkan state machine (ConversationHandler)
- Menambah validasi admin atau user tertentu
- Mengembangkan fitur modular jangka panjang

---

## 🛠 Teknologi
Bot dibangun menggunakan:

- **Python 3.9+**
- **python-telegram-bot v20+**
- **AsyncIO**

---

## 📂 Struktur Project (Minimal)
project/
│── bot.py # File utama bot
│── handlers/ # (Opsional) folder handler untuk bot yang berkembang
│── requirements.txt
└── README.md


---

## 📦 Instalasi & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
2️⃣ Install dependency
pip install python-telegram-bot==20.7

3️⃣ Masukkan BOT TOKEN

Edit file bot.py dan ubah:

TOKEN = "MASUKKAN_TOKEN_BOT_ANDA_DI_SINI"

▶️ Menjalankan Bot

Jalankan bot dengan:

python bot.py


Jika berhasil, Anda akan melihat output:

Bot berjalan... Tekan CTRL + C untuk berhenti.

🧑‍💻 Cara Menambahkan Fitur Baru
➕ Tambah Command Baru

Tambahkan handler di bot.py:

app.add_handler(CommandHandler("namaperintah", fungsi_handler))

➕ Tambah Inline Button (callback)

Gunakan CallbackQueryHandler.

➕ Tambah State (percakapan)

Gunakan ConversationHandler.

➕ Membatasi command untuk admin

Tambahkan filter pada awal handler.

Struktur bot dibuat fleksibel sehingga command atau modul dapat ditambahkan tanpa mengubah arsitektur inti.

🗺 Roadmap Pengembangan

Rencana fitur lanjutan:

/start dengan menu interaktif

Sistem Set Chat (1–3)

Database penyimpanan konfigurasi

Fitur admin-only

Logging & monitoring aktivitas

Fitur broadcast

📄 Lisensi

Project ini bebas dikembangkan dan dimodifikasi sesuai kebutuhan.

💬 Kontribusi

Pull request, issue, atau saran pengembangan sangat diterima.


---
