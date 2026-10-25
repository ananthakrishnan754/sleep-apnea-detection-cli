# Test Commands - CLI Only

After cloning the repo, run these commands one by one to test different cases.

## Setup
```bash
cd sleep-apnea-detection-cli
pip install -r requirements.txt
```

## Test with different input files

### Test 1 - Normal Case 1
```bash
python cli/predict_file.py --input test_inputs/normal_case_1.npy
```

### Test 2 - Normal Case 2
```bash
python cli/predict_file.py --input test_inputs/normal_case_2.npy
```

### Test 3 - Normal Case 3
```bash
python cli/predict_file.py --input test_inputs/normal_case_3.npy
```

### Test 4 - Mild Apnea Case 1
```bash
python cli/predict_file.py --input test_inputs/mild_apnea_4.npy
```

### Test 5 - Mild Apnea Case 2
```bash
python cli/predict_file.py --input test_inputs/mild_apnea_5.npy
```

### Test 6 - Mild Apnea Case 3
```bash
python cli/predict_file.py --input test_inputs/mild_apnea_6.npy
```

### Test 7 - Moderate Apnea Case 1
```bash
python cli/predict_file.py --input test_inputs/moderate_apnea_7.npy
```

### Test 8 - Moderate Apnea Case 2
```bash
python cli/predict_file.py --input test_inputs/moderate_apnea_8.npy
```

### Test 9 - Severe Apnea Case 1
```bash
python cli/predict_file.py --input test_inputs/severe_apnea_9.npy
```

### Test 10 - Severe Apnea Case 2
```bash
python cli/predict_file.py --input test_inputs/severe_apnea_10.npy
```

### Test with TXT format
```bash
python cli/predict_file.py --input test_inputs/normal_case_1.txt
```

### Test with JSON format
```bash
python cli/predict_file.py --input test_inputs/normal_case_1.json
```

## Notes
- Model uses trained weights from `weights/fusion_best.pth`
- Trained on real PhysioNet Apnea-ECG clinical data (no synthetic datasets)
- Results saved to `prediction_result.json`
- Works with .npy, .txt, .json formats
