# Execution Plan (CLI First -> App)

## Done
- [x] Scaffold project structure
- [x] Config with patient-wise split
- [x] User calibration/baseline module
- [x] Watch simulator (degrade clinical -> watch-like)
- [x] Model skeleton (SpectroBranch ResNet18, RRBranch BiLSTM+Attn, SpO2Branch MLP, Fusion)
- [x] CLI: calibrate_user.py, run_demo.py
- [x] Severity/AHI proxy
- [x] Demo with JSON and watch_sim modes

## Next (Priority)
- [ ] Preprocessing scripts (ecg_prep, rr_extract, stft_spectro, spo2_prep)
- [ ] Dataset class with inter-patient split enforcement
- [ ] Training script (train_fusion.py) with ablation order
- [ ] 1D Denoising Autoencoder for RR reconstruction
- [ ] Flask backend (app.py) mirroring CLI logic
- [ ] Flutter app skeleton (Home, Calibrate, Demo, Results, Explain)
- [ ] Create FINAL_PDF with architecture + CLI guide
