# Sleep Apnea Detection System - Project Status Report

**Team:** Irin Babu (FIT23CSD033) | Mariya Jiji (FIT23CSD040) | Neha B S (FIT23CSD044) | Nisha P R (FIT23CSD047)  
**Guide:** Simi Stephen, AP, CSE  
**Project Type:** Explainable Sleep Apnea Detection using ECG + SpO2 with Watch-Simulated Data  
**Date:** October 2026

## 1. Objective
To build an explainable Sleep Apnea Detection system using ECG, HR, and SpO2 with a hybrid model (CNN-BiLSTM + Attention + Grad-CAM), served via a Flask backend and a Flutter Android app. As per requirement, no external hardware integration is done. Instead, we use a "Run Demo" mode with simulated smartwatch/watch data.

## 2. What Has Been Done

### 2.1 Research & Architecture
- [x] Analyzed base paper (SleepECG-Net) and 5 recent papers
- [x] Created enhanced architecture with dual-view fusion
- [x] Finalized fusion approach: Spectrogram (ResNet18) + RR Sequence (1D-CNN + BiLSTM + Attention) + SpO2 Features (MLP)
- [x] Addressed train-test leakage with strict inter-patient split
- [x] Incorporated personalization via per-user baseline calibration
- [x] Added AHI-proxy and severity classification
- [x] Added signal reconstruction/denoising idea (1D Denoising Autoencoder for RR)

### 2.2 CLI Prototype (Fully Working)
- [x] `cli/calibrate_user.py` - User calibration using HR data to compute baseline
- [x] `cli/run_demo.py` - Run demo in `watch_sim` or `json` mode
- [x] Shows prediction, confidence, AHI-proxy, severity, user baseline
- [x] Clearly labels "SIMULATED WATCH DATA"
- [x] Shows branches used and explainability info

### 2.3 Preprocessing Pipeline
- [x] `preprocessing/ecg_prep.py` - Bandpass filtering (0.5-40 Hz)
- [x] `preprocessing/rr_extract.py` - R-peak detection & RR interval extraction
- [x] `preprocessing/stft_spectro.py` - STFT spectrogram generation (resized to 224x224)
- [x] `preprocessing/spo2_prep.py` - SpO2 feature extraction (9 features)
- [x] `preprocessing/watch_prep.py` ready for watch-format inputs

### 2.4 Model Architecture
- [x] `models/resnet_ecg.py` - Spectrogram branch (ResNet18 adapted)
- [x] `models/rr_bilstm.py` - RR branch (Conv1D + BiLSTM + Additive Attention)
- [x] `models/spo2_mlp.py` - SpO2 feature branch
- [x] `models/fusion_model.py` - Embedding-level fusion
- [x] `models/recon_ae.py` - 1D RR Denoising Autoencoder

### 2.5 Utilities
- [x] `utils/baseline.py` - User profile & calibration
- [x] `utils/watch_sim.py` - Degrade clinical ECG to watch-like (HR/RR/SpO2)
- [x] `utils/severity.py` - AHI-proxy and severity bins
- [x] `utils/explain.py` - Explainer skeleton
- [x] `utils/splits.py` - Split enforcement logic

### 2.6 Backend (Flask)
- [x] `backend/app.py` - Endpoints: `/health`, `/predict`, `/calibrate`
- [x] CORS enabled for Flutter app
- [x] Returns structured JSON with prediction, confidence, AHI, severity

### 2.7 Flutter App (UI Stitched)
- [x] Dark themed UI (SleepSync design)
- [x] `HomeScreen` - Navigation hub
- [x] `CalibrateScreen` - User baseline calibration
- [x] `DemoScreen` - Run demo with watch simulation
- [x] `ResultsScreen` - Prediction results with AHI/severity
- [x] `ExplainScreen` - Grad-CAM, Attention, LIME, RR Reconstruction
- [x] Widgets: GradientCard, StatusBadge
- [x] API service to connect with Flask
- [x] "SIMULATED WATCH DATA" badge throughout

### 2.8 Documentation & Config
- [x] `configs/config.yaml` - Inter-patient split, spectrogram params
- [x] `requirements.txt` - Dependencies
- [x] `FINAL_IMPLEMENTATION_GUIDE.md`
- [x] `COMPLETE_PROJECT_GUIDE.pdf`
- [x] Multiple architecture guides & PDFs

## 3. What Needs To Be Done

### 3.1 Data Preparation
- [ ] Download PhysioNet Apnea-ECG dataset
- [ ] Parse WFDB files and extract 60s windows
- [ ] Apply strict inter-patient split using `splits.json`
- [ ] Generate spectrograms on-the-fly or cache efficiently
- [ ] Handle class imbalance

### 3.2 Training
- [ ] Implement full `data/dataset.py` with windowing logic
- [ ] Complete `train/train_fusion.py` with actual training loop
- [ ] Train in order: spectrogram-only -> RR-only -> dual-view -> fusion+SpO2
- [ ] Use Focal Loss with class weights
- [ ] Save checkpoints to `weights/`
- [ ] Log metrics (accuracy, sensitivity, specificity, AHI-correlation)

### 3.3 Explainability Integration
- [ ] Implement actual Grad-CAM for ResNet18
- [ ] Extract and visualize attention weights from BiLSTM
- [ ] Implement LIME wrapper for fused model
- [ ] Train/evaluate RR Denoising Autoencoder
- [ ] Generate explanation images for app

### 3.4 App Integration
- [ ] Connect Flutter app to actual trained model via Flask
- [ ] Display spectrogram, RR plot, attention heatmap
- [ ] Add real Grad-CAM visualization
- [ ] Handle actual API responses
- [ ] Test on emulator/device

### 3.5 Final Touches
- [ ] Ablation study results
- [ ] Update README with full instructions
- [ ] Prepare demo for 26th presentation
- [ ] Clean up and test end-to-end

## 4. How To Run Right Now

### CLI Test
```bash
cd /home/ananthakrishnan/sleep_apnea_proto
python3 cli/calibrate_user.py --user demo --hr_json data/watch_sim/demo_hr.json
python3 cli/run_demo.py --mode watch_sim --record a01 --user demo
```

### Backend
```bash
cd /home/ananthakrishnan/sleep_apnea_proto
python3 backend/app.py
```

### Flutter App
```bash
cd /home/ananthakrishnan/sleep_apnea_proto/flutter_app
flutter pub get
flutter run
```

## 5. Key Notes
- **No external hardware** - Everything is simulated
- **Module by module** approach ready for prototype presentation
- **Personalization** implemented via user calibration
- **Explainable** with Grad-CAM, Attention, LIME
- **Watch-compatible** architecture using HR/RR/SpO2 features
- **Fusion at embedding level** as planned
