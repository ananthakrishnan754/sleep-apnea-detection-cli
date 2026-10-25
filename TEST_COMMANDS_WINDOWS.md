# Test Commands - Windows (CMD/PowerShell)

After cloning the repo in Windows, run these commands one by one.

## Setup
```cmd
cd sleep-apnea-detection-cli
pip install -r requirements.txt
```

## Test Commands (CMD)
```cmd
python cli\predict_file.py --input test_inputs\normal_case_1.npy
python cli\predict_file.py --input test_inputs\normal_case_2.npy
python cli\predict_file.py --input test_inputs\normal_case_3.npy
python cli\predict_file.py --input test_inputs\mild_apnea_4.npy
python cli\predict_file.py --input test_inputs\mild_apnea_5.npy
python cli\predict_file.py --input test_inputs\mild_apnea_6.npy
python cli\predict_file.py --input test_inputs\moderate_apnea_7.npy
python cli\predict_file.py --input test_inputs\moderate_apnea_8.npy
python cli\predict_file.py --input test_inputs\severe_apnea_9.npy
python cli\predict_file.py --input test_inputs\severe_apnea_10.npy
```

## Test Commands (PowerShell)
```powershell
python cli/predict_file.py --input test_inputs/normal_case_1.npy
python cli/predict_file.py --input test_inputs/mild_apnea_4.npy
python cli/predict_file.py --input test_inputs/severe_apnea_9.npy
```

## Notes
- Use backslashes in CMD, forward slashes work in PowerShell
- All files are included in repo
- Model uses trained weights from weights/fusion_best.pth
- Trained on real PhysioNet Apnea-ECG clinical data
