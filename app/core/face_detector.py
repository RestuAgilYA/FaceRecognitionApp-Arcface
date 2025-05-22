from facenet_pytorch import MTCNN
from PIL import Image
import numpy as np

# Sesuaikan ukuran wajah crop akhir dengan model ONNX kamu
IMAGE_SIZE = 368

# Buat MTCNN tanpa auto resize, karena kita ingin ambil bounding box saja
mtcnn = MTCNN(keep_all=True, device='cpu')

def detect_face(image: Image.Image):
    """
    Deteksi wajah dari gambar dan crop wajah pertama yang ditemukan.

    Returns:
        face_crop_np (np.ndarray): Gambar wajah hasil crop dalam format (H, W, C)
    """
    try:
        # Deteksi bounding box wajah
        boxes, probs = mtcnn.detect(image)

        # Jika tidak ada wajah terdeteksi
        if boxes is None or len(boxes) == 0:
            print("❌ Tidak ada wajah terdeteksi")
            return None

        # Ambil wajah dengan probabilitas tertinggi
        best_idx = int(np.argmax(probs))
        box = boxes[best_idx]  # Format: (x1, y1, x2, y2)
        x1, y1, x2, y2 = map(int, box)

        # Crop wajah dari gambar asli
        face_crop = image.crop((x1, y1, x2, y2)).resize((IMAGE_SIZE, IMAGE_SIZE))
        face_crop_np = np.array(face_crop)

        # Validasi hasil
        if face_crop_np.ndim != 3 or face_crop_np.shape[2] != 3:
            print("⚠️ Gambar wajah tidak valid:", face_crop_np.shape)
            return None

        return face_crop_np

    except Exception as e:
        print(f"🔥 Error saat mendeteksi wajah: {e}")
        return None