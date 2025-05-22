# 🧠 Face Recognition App – ArcFace
**Knowledge Test – AI Engineer (Computer Vision)**  
**PT Widya Inovasi Indonesia**

---

## 📸 Deskripsi

Sistem ini merupakan aplikasi Face Recognition end-to-end berbasis Deep Learning menggunakan:
- ✅ **FastAPI** untuk REST API
- ✅ **ArcFace ONNX model** untuk ekstraksi fitur wajah
- ✅ **MTCNN** untuk deteksi wajah
- ✅ **PostgreSQL** untuk menyimpan data embedding wajah
- ✅ **Docker** untuk kemudahan deployment

---
STEP 1:

## 🚀 Jalankan Aplikasi dengan Docker

### 1. Clone repositori

```bash
git clone https://github.com/RestuAgilYA/FaceRecognitionApp-Arcface.git
cd FaceRecognitionApp-Arcface
```

---
STEP 2:
## 📥 Download Model `arcface.onnx`

> Karena GitHub membatasi ukuran file (maks. 100MB), file model `arcface.onnx` **tidak disertakan dalam repositori**.

## Silakan Download dari link berikut:

📎 [Download arcface.onnx via Hugging Face] (https://huggingface.co/FoivosPar/Arc2Face/resolve/da2f1e9aa3954dad093213acfc9ae75a68da6ffd/arcface.onnx?download=true)

ATAU / OR

📎 [Download arcface.onnx via Google Drive](https://drive.google.com/file/d/1oKa0_0Z4_YVfBSd1zIVpYT_JkZ7OrgLt/view?usp=sharing)

> Setelah diunduh, letakkan ke folder `models/`, jika folder belum ada, silakan buat folder dengan nama 'models':

models/
└── arcface.onnx

---

STEP 3

### 2. Jalankan Docker
```bash
docker-compose up --build
```

### 3. Akses Aplikasi
http://localhost:8000

---


Struktur Folder:
.
├── app/
│ ├── api/                # FastAPI routes
│ ├── core/               # Face detector, feature extractor, matcher
│ ├── db/                 # SQLAlchemy models & database config
│ └── main.py             # FastAPI entry point
├── frontend/             # HTML + Tailwind UI
├── models/               # (letakkan arcface.onnx di sini)
├── static/images/        # hasil crop wajah
├── Dockerfile            # Container instructions
├── docker-compose.yml    # Run FastAPI + PostgreSQL together
├── .env                  # Database connection string
├── requirements.txt      # Python dependencies
└── README.md             # This file

🔧 API Endpoint
| Method | Endpoint              | Fungsi                             |
| ------ | --------------------- | ---------------------------------- |
| GET    | `/api/face`           | List wajah yang terdaftar          |
| POST   | `/api/face/register`  | Register wajah baru (name + image) |
| POST   | `/api/face/recognize` | Kenali wajah dari file upload      |
| DELETE | `/api/face/{id}`      | Hapus wajah dari database          |

UI Web Fitur
📤 Register wajah
📷 Unggah gambar untuk mengenali wajah
🗑️ Hapus wajah
🔍 Lihat daftar wajah

---

## ⚙️ menjalankan Aplikasi secara manual (tanpa Docker)

1. Install dependencies
```bash
- pip install -r requirements.txt
```
2. Siapkan file .env
```bash
- DATABASE_URL=postgresql://restu:yourpassword@localhost:5432/face_db
```

3. Jalankan server
```bash
- uvicorn app.main:app --reload
````
---

📎 Catatan Tambahan
- Embedding wajah disimpan dalam DB dengan format pickle

- Image crop wajah disimpan ke dalam static/images

- Model arcface.onnx harus tersedia untuk sistem bekerja

---

🙌 Terima kasih
Aplikasi ini dikembangkan sebagai bagian dari Knowledge Test
untuk posisi AI Engineer – PT Widya Inovasi Indonesia
