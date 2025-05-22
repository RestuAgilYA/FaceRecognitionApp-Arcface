from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db import models
from app.core.face_detector import detect_face
from app.core.feature_extractor import get_embedding
from app.core.matcher import find_best_match
import numpy as np
import pickle
from PIL import Image
from app.db import schemas
import uuid
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/face", response_model=list[schemas.Face])
def get_faces(db: Session = Depends(get_db)):
    try:
        faces = db.query(models.Face).all()
        print(f"📦 Jumlah data di database: {len(faces)}")
        return faces
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/face/register")
def register_face(name: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        image = Image.open(file.file).convert("RGB")
        face_crop = detect_face(image)

        if face_crop is None:
            raise HTTPException(status_code=400, detail="❌ Face not detected")

        embedding = get_embedding(face_crop)
        embedding_bytes = pickle.dumps(embedding)

        # Simpan wajah sementara tanpa path
        face_entry = models.Face(name=name, embedding=embedding_bytes)
        db.add(face_entry)
        db.commit()
        db.refresh(face_entry)

        # Simpan gambar ke filesystem
        image_filename = f"face_{face_entry.id}.jpg"
        image_path = os.path.join("static", "images", image_filename)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        face_crop_pil = Image.fromarray(face_crop)
        face_crop_pil.save(image_path)

        # Update path di DB
        face_entry.image_path = image_path
        db.commit()

        return {"id": face_entry.id, "name": name, "image_path": image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/face/recognize")
def recognize_face(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        image = Image.open(file.file).convert("RGB")
        face_crop = detect_face(image)

        if face_crop is None:
            raise HTTPException(status_code=400, detail="❌ Face not detected")

        if face_crop.ndim != 3 or face_crop.shape[2] != 3:
            raise HTTPException(status_code=400, detail=f"❌ Invalid face image shape: {face_crop.shape}")

        embedding = get_embedding(face_crop)
        print(f"🔍 Recognized embedding (first 5): {embedding[:5]}")

        faces = db.query(models.Face).all()

        if not faces:
            return {"match": "not found", "reason": "no faces in database"}

        db_embeddings = [pickle.loads(f.embedding) for f in faces]

        # Debug similarity for each face
        from sklearn.metrics.pairwise import cosine_similarity
        print("🔎 Similarities to DB:")
        for i, db_emb in enumerate(db_embeddings):
            sim = cosine_similarity(embedding.reshape(1, -1), db_emb.reshape(1, -1))[0][0]
            print(f" - ID {faces[i].id}, Name: {faces[i].name}, Similarity: {sim:.4f}")

        index, similarity = find_best_match(embedding, db_embeddings)

        if index is not None:
            return {
                "id": faces[index].id,
                "name": faces[index].name,
                "similarity": similarity
            }
        else:
            return {"match": "not found"}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/api/face/{id}")
def delete_face(id: int, db: Session = Depends(get_db)):
    face = db.query(models.Face).filter(models.Face.id == id).first()
    if not face:
        raise HTTPException(status_code=404, detail="Face not found")
    db.delete(face)
    db.commit()
    return {"message": "Face deleted"}