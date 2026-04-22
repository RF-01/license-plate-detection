# License Plate Detection

A computer vision object detection project that detects and localizes license plates in vehicle images. We train and compare multiple detection architectures (YOLOv8, Faster R-CNN, RetinaNet) and analyze their performance.

## Project Structure
```
license-plate-detection/
├── notebooks/                # Jupyter notebooks for exploration & analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_train_yolov8.ipynb
│   ├── 04_train_frcnn_retinanet.ipynb
│   ├── 05_evaluation.ipynb
│   └── license_plate_detection.ipynb  # Combined notebook (all phases, with outputs)
├── src/                      # Source code / utility scripts
├── configs/                  # Model training configs
├── data/                     # Dataset (not pushed to GitHub)
│   ├── raw/                  # Original dataset from Kaggle
│   └── processed/            # Processed/split dataset
├── models/                   # Saved model weights (not pushed to GitHub)
├── results/                  # Evaluation results, plots, metrics
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

## Dataset

- **Name:** Car Plate Detection (Kaggle)
- **Content:** 433 images with annotated bounding boxes around license plates
- **Source:** https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/RF-01/license-plate-detection.git
cd license-plate-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Download from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection) and extract into `data/raw/`.

### 4. Run the notebook
Open `notebooks/license_plate_detection.ipynb` in Google Colab or Jupyter. All phases are included — models are loaded from saved weights, no retraining needed.

## Models Compared

| Model | Architecture Type | Key Characteristics |
|-------|------------------|---------------------|
| YOLOv8n | Single-stage | Best accuracy (93.1% mAP@50), fastest, edge-deployable |
| YOLOv8s | Single-stage | Larger capacity, overfits on small datasets |
| Faster R-CNN | Two-stage | Strong accuracy, slow inference (5.1 FPS on GPU) |
| RetinaNet | Single-stage | Focal loss, lowest accuracy on single-class data |

## Results

| Model | mAP@50 | mAP@50:95 | FPS (GPU) |
|-------|--------|-----------|-----------|
| YOLOv8n | 0.9314 | 0.5437 | 37.6 |
| YOLOv8s | 0.8953 | 0.5170 | 32.6 |
| Faster R-CNN | 0.9064 | 0.5335 | 5.1 |
| RetinaNet | 0.8820 | 0.5036 | 7.9 |

## Team Members
- Roda Fadlallah
- Ramez Kanj
- Mohammad Nahhal
- Mohammad Rizk

## License
This project is for educational purposes.