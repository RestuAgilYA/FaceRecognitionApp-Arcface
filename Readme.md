# 🧠 Face Recognition App – ArcFace
**Knowledge Test – AI Engineer (Computer Vision)**  
**PT Widya Inovasi Indonesia**
---

🟢 App akan tampil di:  
📍 http://localhost:8000/  
jika sudah mengikuti petunjuk di bawah ini.

---

## 📸 Deskripsi

Sistem ini merupakan aplikasi Face Recognition end-to-end berbasis Deep Learning menggunakan:
- ✅ **FastAPI** untuk REST API
- ✅ **ArcFace (ONNX)** untuk ekstraksi fitur wajah
- ✅ **MTCNN** untuk deteksi wajah
- ✅ **PostgreSQL** sebagai penyimpanan data wajah
- ✅ **Docker** untuk kemudahan deployment

---

## 🚀 Langkah Menjalankan Aplikasi (Rekomendasi: Docker)

### 📦 STEP 1: Clone Repositori

```bash
git clone https://github.com/RestuAgilYA/FaceRecognitionApp-Arcface.git
cd FaceRecognitionApp-Arcface
````

---

### 📥 STEP 2: Download Model `arcface.onnx`

> Karena GitHub membatasi ukuran file (maks. 100MB), file model `arcface.onnx` **tidak disertakan dalam repositori**.

Silakan unduh melalui salah satu link berikut:

* 📎 [Download via Hugging Face](https://huggingface.co/FoivosPar/Arc2Face/resolve/da2f1e9aa3954dad093213acfc9ae75a68da6ffd/arcface.onnx?download=true)
* 📎 [Download via Google Drive](https://drive.google.com/file/d/1oKa0_0Z4_YVfBSd1zIVpYT_JkZ7OrgLt/view?usp=sharing)

🗂 Setelah diunduh, letakkan di dalam folder `models/`:

```
models/
└── arcface.onnx
```

---

### 🐳 STEP 3: Jalankan Aplikasi dengan Docker

```bash
docker pull restuagilya/face-recognition-app:latest
```
### Apabila anda menjalankan di Powershell:
```bash
docker run -p 8000:8000 --env-file .env -v "${PWD}/models:/app/models" restuagilya/face-recognition-app:latest
```
### Apabila anda menjalankan di Command Prompt:
```bash
docker run -p 8000:8000 --env-file .env -v "%cd%\models:/app/models" restuagilya/face-recognition-app:latest
```

### 🌐 Akses Aplikasi:

* [http://localhost:8000](http://localhost:8000)

---

## 📁 Struktur Folder

```bash
.
├── app/
│   ├── api/                # FastAPI routes
│   ├── core/               # Face detector, feature extractor, matcher
│   ├── db/                 # SQLAlchemy models & database config
│   └── main.py             # FastAPI entry point
├── frontend/               # HTML + Tailwind UI
├── models/                 # (letakkan arcface.onnx di sini)
├── static/images/          # Hasil crop wajah
├── Dockerfile              # Container instructions
├── docker-compose.yml      # Jalankan FastAPI + PostgreSQL bersama
├── .env                    # Koneksi database
├── requirements.txt        # Python dependencies
└── README.md               # File ini
```

---

## 🔧 API Endpoints

| Method | Endpoint              | Fungsi                             |
| ------ | --------------------- | ---------------------------------- |
| GET    | `/api/face`           | List wajah yang terdaftar          |
| POST   | `/api/face/register`  | Register wajah baru (name + image) |
| POST   | `/api/face/recognize` | Kenali wajah dari file upload      |
| DELETE | `/api/face/{id}`      | Hapus wajah dari database          |

---

## 💻 UI Web Fitur

* 📤 Register wajah
* 📷 Unggah gambar untuk dikenali
* 🗑️ Hapus wajah dari database
* 🔍 Lihat daftar wajah yang telah terdaftar

---

## ⚙️ Menjalankan Aplikasi Tanpa Docker (Manual)

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan server

```bash
uvicorn app.main:app --reload
```

---

## 📝 Catatan Tambahan

* Embedding wajah disimpan dalam database menggunakan `pickle`
* Gambar hasil crop disimpan di `static/images`
* File `arcface.onnx` **harus tersedia** agar sistem bisa berjalan

---

## 🙌 Terima Kasih

Aplikasi ini dikembangkan sebagai bagian dari **Knowledge Test**
untuk posisi **AI Engineer** di **PT Widya Inovasi Indonesia**.

Jika Anda mengalami kendala dalam menjalankan aplikasi, silakan hubungi saya melalui email: restuagil.ya@gmail.com atau GitHub.

---
