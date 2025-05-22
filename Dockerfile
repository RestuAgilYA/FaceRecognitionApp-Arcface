FROM python:3.10-slim

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Salin seluruh isi project
COPY . .

# Install python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Jalankan FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]