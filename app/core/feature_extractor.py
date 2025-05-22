import onnxruntime as ort
import numpy as np
import cv2
import os

model_path = os.path.join("models", "arcface.onnx")
session = ort.InferenceSession(model_path)

def preprocess_face(face_img):
    face = cv2.resize(face_img, (112, 112))
    face = face.astype("float32") / 255.0
    face = np.transpose(face, (2, 0, 1))  # HWC to CHW
    face = np.expand_dims(face, axis=0)  # Add batch dim
    return face

def get_embedding(face_img: np.ndarray) -> np.ndarray:
    try:
        img = preprocess_face(face_img)  # Gunakan preprocessing yang benar
        input_name = session.get_inputs()[0].name  # Hindari hardcoding

        output = session.run(None, {input_name: img})[0]
        print("Embedding shape:", output.shape)

        embedding = np.ravel(output)
        return embedding
    except Exception as e:
        print("❌ Error saat ekstraksi fitur:", e)
        raise