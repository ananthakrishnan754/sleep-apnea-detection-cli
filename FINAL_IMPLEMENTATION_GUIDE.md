# Sleep Apnea Detection - Final Implementation Guide
CLI Prototype + App Ready

## Quick Start (CLI)
```bash
cd sleep_apnea_proto
pip install -r requirements.txt
python cli/calibrate_user.py --user demo --hr_json data/watch_sim/demo_hr.json
python cli/run_demo.py --mode watch_sim --record a01 --user demo
python cli/run_demo.py --mode json --input data/watch_sim/sample_watch.json --user demo
```

## Architecture
- View-A: ECG Spectrogram (STFT) -> ResNet18 -> 256
- View-B: RR sequence -> Conv1D + BiLSTM + Attention -> 256
- View-C: SpO2/watch features (9) -> MLP -> 16
- Fusion: concat(528) -> FC(256)->ReLU->Dropout->FC(2)

## Key Features
- Inter-patient split enforced
- Watch-sim degradation
- User baseline/personalization
- RR denoising autoencoder (reconstruction idea)
- AHI proxy + severity
- Grad-CAM + attention + LIME ready
- Demo labeled as SIMULATED
