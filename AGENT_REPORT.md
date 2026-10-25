# AGENT REPORT

## Repo state inspection
data/user_profiles: dir
---
user_profiles
---
---
#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
    return jsonify({'status':'ok','simulated_spo2':True})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}
    return jsonify({
        'prediction': 'APNEA_SUSPECTED',
        'confidence': 0.87,
        'ahi_proxy': 12.4,
        'severity': 'Moderate',
        'simulated': True,
        'note': 'Demo mode - uses watch-simulated values',
        'branches': ['spectrogram_resnet18','rr_bilstm_attention','spo2_mlp']
    })

@app.route('/calibrate', methods=['POST'])
def calibrate():
    return jsonify({'calibrated': True})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
---
#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.baseline import UserProfile
from utils.watch_sim import WatchSim
from utils.severity import ahi_proxy, severity
import torch

def main():
    ap = argparse.ArgumentParser(description='Sleep Apnea CLI Demo')
    ap.add_argument('--mode', choices=['watch_sim','json'], default='watch_sim')
    ap.add_argument('--record', default='a01')
    ap.add_argument('--user', default='demo')
    ap.add_argument('--input', default='data/watch_sim/sample_watch.json')
    args = ap.parse_args()

    print('='*60)
    print('SLEEP APNEA DETECTION - CLI PROTOTYPE')
    print('='*60)
    print(f'Mode: {args.mode} | Record: {args.record} | User: {args.user}')
    print(f'Time: {time.strftime("%Y-%m-%d %H:%M:%S")}')
    print('='*60)

    prof = UserProfile(args.user)
    prof.load()
    if prof.calibrated:
        print(f'[USER CALIBRATION] baseline_hr={prof.baseline_hr:.1f} | thresh={prof.hr_thresh:.1f}')
    else:
        print('[USER CALIBRATION] NOT CALIBRATED (run cli/calibrate_user.py)')

    if args.mode == 'json':
        with open(args.input) as f:
            data = json.load(f)
        print(f'[INPUT] Loaded watch JSON - SIMULATED: {data.get("simulated",False)}')
        hr = data.get('hr',[])
        spo2 = data.get('spo2',[])
        rr = data.get('rr_intervals',[])
        print(f'[WATCH] HR samples: {len(hr)} | SpO2 samples: {len(spo2)} | RR samples: {len(rr)}')
    else:
        sim = WatchSim()
        print(f'[WATCH-SIM] Degrading clinical data from {args.record} to watch-like...')
        hr = [76,77,78,80,79,81,82,84,83,82,80,78,77,76,75]
        rr = sim.degrade_from_ecg_rr([0.78]*15)
        spo2 = sim.make_spo2(apnea_mask_1min=0.8)
        print(f'[WATCH-SIM] Generated watch-like HR/RR/SpO2 (SIMULATED)')

    # Dummy inference for demo
    pred = 'APNEA SUSPECTED'
    conf = 0.87
    hours = 1.0
    pred_min = int(conf*60)
    ahi = ahi_proxy(pred_min, hours)
    sev = severity(ahi)

    print('\n'+'-'*60)
    print('PREDICTION')
    print('-'*60)
    print(f'Result: {pred}')
    print(f'Confidence: {conf:.2%}')
    print(f'AHI-proxy: {ahi:.1f} events/hour')
    print(f'Severity: {sev}')
    print('-'*60)
    print('\n[EXPLAINABILITY] Branches used: Spectrogram(ResNet18)+RR(BiLSTM+Attn)+SpO2(MLP)')
    print('[EXPLAINABILITY] Grad-CAM on layer4[-1], Attention weights over beats')
    print('[DEMO NOTICE] SpO2 shown is SIMULATED for demo purposes')
    print('='*60)

if __name__=='__main__':
    main()

## Findings
- models/: stubs/skeletons mostly (modules exist, no trained weights)
- train/: train_fusion.py exists but minimal
- data/: structure exists, likely no real downloaded data yet
- backend/app.py returns hardcoded predictions (PLACEHOLDER) - marked as issue
- cli/run_demo.py has dummy inference - needs real model loading
- weights/: empty (0 files)
- splits.json: missing (only in config.yaml)
- Flutter app: UI stitched, not connected to real trained model
