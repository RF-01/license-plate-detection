# Colab Setup & Training Guide
# ================================
# Use this script in Google Colab (Runtime > Change runtime type > T4 GPU)
# This handles: dataset download, repo cloning, and training.

# ============================================================
# CELL 1: Verify GPU is available
# ============================================================
import torch
print(f"GPU Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
else:
    print("WARNING: No GPU detected! Go to Runtime > Change runtime type > T4 GPU")

# ============================================================
# CELL 2: Clone your GitHub repo
# ============================================================
# !git clone https://github.com/YOUR_USERNAME/license-plate-detection.git
# %cd license-plate-detection

# ============================================================
# CELL 3: Install dependencies
# ============================================================
# !pip install -r requirements.txt

# ============================================================
# CELL 4: Download dataset from Kaggle
# ============================================================
# Upload your kaggle.json first:
# from google.colab import files
# files.upload()
# !mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
# !kaggle datasets download -d andrewmvd/car-plate-detection
# !unzip -q car-plate-detection.zip -d data/raw/

# ============================================================
# CELL 5: Run training (uncomment the model you want to train)
# ============================================================
# !python train_yolo.py
# !python train_frcnn.py
# !python train_retinanet.py

# ============================================================
# CELL 6: Push results back to GitHub
# ============================================================
# !git add results/
# !git commit -m "Add training results"
# !git push
