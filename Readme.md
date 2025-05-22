# 🧠 Face Recognition System – Knowledge Test  
**PT Widya Inovasi Indonesia – AI Engineer (Computer Vision)**

This is an end-to-end face recognition system implemented using **FastAPI**, **ONNX (ArcFace)**, and **PostgreSQL**. The system supports face registration, recognition, and deletion using deep learning-based facial embeddings.

---

## 🚀 Features

- ✅ Face Detection (MTCNN)
- ✅ Feature Extraction (ArcFace - ONNX)
- ✅ Face Matching (Cosine Similarity)
- ✅ REST API (FastAPI)
- ✅ PostgreSQL database with face embeddings
- ✅ HTML Frontend (Tailwind CSS)
- ✅ Static Image Saving
- ✅ Docker & Docker Compose Support

---

## 🛠️ Technologies Used

- **Backend:** Python, FastAPI, SQLAlchemy
- **Model:** ONNX (ArcFace)
- **Face Detection:** MTCNN (facenet-pytorch)
- **Frontend:** HTML + TailwindCSS
- **Database:** PostgreSQL
- **Containerization:** Docker + Docker Compose

---

## 📂 Folder Structure

├── app/
│ ├── api/ # FastAPI routes
│ ├── core/ # Face detector, feature extractor, matcher
│ ├── db/ # SQLAlchemy models & database config
│ └── main.py # FastAPI entry point
├── frontend/ # index.html UI
├── models/ # arcface.onnx model
├── static/images/ # Saved face images
├── .env # Database connection string
├── Dockerfile # Container instructions
├── docker-compose.yml # Run FastAPI + PostgreSQL together
├── requirements.txt # Python dependencies
└── README.md # This file

---

## ⚙️ Environment Variables

Create a `.env` file (already included in this repo):

---

## 📦 Installation with Docker (RECOMMENDED ✅)

> No need to install PostgreSQL, Python, or ONNX manually.

### 1. Clone this repository

```bash
git clone <YOUR-REPO-LINK>
cd <repo-folder>

### 2. Run the System

```bash
docker-compose up --build

The API will be available at:
📎 http://localhost:8000
📄 HTML UI: http://localhost:8000/static/frontend/index.html



🙏 Acknowledgement
Developed as a part of the Knowledge Test
AI Engineer (Computer Vision) – PT Widya Inovasi Indonesia