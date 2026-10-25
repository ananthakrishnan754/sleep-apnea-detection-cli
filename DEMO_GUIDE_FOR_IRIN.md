# Sleep Apnea Detection - Demo Guide for Students

## Quick Start (CLI)

### Prerequisites
```bash
cd sleep-apnea-detection-cli
pip install -r requirements.txt
```

### Run CLI Demo
```bash
# Simulated watch data demo (with "SIMULATED WATCH DATA" label)
python cli/run_demo.py --mode watch_sim

# JSON input mode
python cli/run_demo.py --mode json
```

## Flask GUI (Recommended for Demo)

### Start Server
```bash
python backend/app.py
```
Server runs at: `http://localhost:5000`

### API Endpoints
- `GET /health` - Check model status
- `POST /predict` - Predict from ECG data
- `POST /calibrate` - Calibrate for user baseline

### Web Interface Features
- Drag & drop ECG/HR/SpO2 files
- Parameter sliders for manual input
- Real-time prediction with confidence
- Explainability (Grad-CAM/Attention visualization)
- Shows "SIMULATED WATCH DATA" when using demo mode

## Model Details
- Architecture: CNN-BiLSTM + Attention
- Input: 60s ECG windows (6000 samples @ 100Hz)
- Output: Apnea/Normal classification
- Trained on PhysioNet Apnea-ECG subset
- Model file: `weights/fusion_best.pth`

## Testing with Sample Inputs
The model accepts various input formats. Use the web interface for easiest demo.

## Commands to Show
```bash
# 1. Check model loads
python -c "import torch; m=torch.load('weights/fusion_best.pth'); print('OK')"

# 2. Run CLI demo
python cli/run_demo.py --mode watch_sim

# 3. Start web server
python backend/app.py
```
