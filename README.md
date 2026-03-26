# License Plate Detection

A computer vision object detection project that detects and localizes license plates in vehicle images. We train and compare multiple detection architectures (YOLOv8, Faster R-CNN, RetinaNet) and analyze their performance.

## Project Structure

```
license-plate-detection/
├── notebooks/                # Jupyter notebooks for exploration & analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_evaluation.ipynb
│   └── 04_results_analysis.ipynb
├── src/                      # Source code / utility scripts
│   ├── data_utils.py
│   ├── evaluate.py
│   └── visualize.py
├── configs/                  # Model training configs
├── data/                     # Dataset (not pushed to GitHub)
│   ├── raw/                  # Original dataset from Kaggle
│   └── processed/            # Processed/split dataset
├── models/                   # Saved model weights (not pushed to GitHub)
├── results/                  # Evaluation results, plots, metrics
├── train_yolo.py             # YOLO training script (for Colab)
├── train_frcnn.py            # Faster R-CNN training script (for Colab)
├── train_retinanet.py        # RetinaNet training script (for Colab)
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
git clone https://github.com/YOUR_USERNAME/license-plate-detection.git
cd license-plate-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Download from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection) and extract into `data/raw/`.

### 4. Training (Google Colab)
Upload the training scripts (`train_yolo.py`, etc.) to Google Colab with a T4 GPU runtime for faster training.

## Models Compared

| Model | Architecture Type | Key Characteristics |
|-------|------------------|---------------------|
| YOLOv8 | Single-stage | Fast, real-time detection |
| Faster R-CNN | Two-stage | High accuracy, slower inference |
| RetinaNet | Single-stage | Focal loss, handles class imbalance |

## Team Members
- (Add your team members here)

## License
This project is for educational purposes.
