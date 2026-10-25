#!/usr/bin/env python3
import argparse
import json
import os
import sys
import numpy as np
import torch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.fusion_model import SleepApneaFusion
from preprocessing.stft_spectro import ecg_to_spectrogram
from preprocessing.rr_extract import extract_rr
from preprocessing.spo2_prep import spo2_features

def main():
    ap = argparse.ArgumentParser(description='Predict Sleep Apnea from ECG file using trained model')
    ap.add_argument('--input', required=True, help='Path to ECG file (.npy, .txt, or .json)')
    ap.add_argument('--spo2', help='Path to SpO2 file or comma separated values')
    ap.add_argument('--model', default='weights/fusion_best.pth')
    args = ap.parse_args()
    
    print('='*60)
    print('SLEEP APNEA DETECTION - MODEL PREDICTION')
    print('='*60)
    print('Loading trained model...')
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = SleepApneaFusion(use_spo2=True)
    state = torch.load(args.model, map_location=device)
    model.load_state_dict(state, strict=False)
    model.to(device)
    model.eval()
    print(f'Model loaded from {args.model}')
    print('='*60)
    
    if args.input.endswith('.npy'):
        ecg = np.load(args.input)
        if ecg.ndim > 1:
            ecg = ecg.flatten()
    elif args.input.endswith('.json'):
        with open(args.input) as f:
            data = json.load(f)
        ecg = np.array(data.get('ecg', data.get('signal', [])))
    else:
        ecg = np.loadtxt(args.input)
        if ecg.ndim > 1:
            ecg = ecg[:,0]
    
    print(f'Loaded ECG: {len(ecg)} samples')
    
    if args.spo2:
        if os.path.isfile(args.spo2):
            if args.spo2.endswith('.npy'):
                spo2_arr = np.load(args.spo2)
            elif args.spo2.endswith('.json'):
                with open(args.spo2) as f:
                    d = json.load(f)
                spo2_arr = np.array(d.get('spo2', []))
            else:
                spo2_arr = np.loadtxt(args.spo2)
        else:
            spo2_arr = np.array([float(x) for x in args.spo2.split(',')])
    else:
        spo2_arr = np.ones(9) * 95
    
    with torch.no_grad():
        ecg_seg = ecg[:6000] if len(ecg) >= 6000 else np.pad(ecg, (0,6000-len(ecg)))
        spec = ecg_to_spectrogram(ecg_seg)
        spec = spec[:1, :, :]  # take only first channel
        spec_t = torch.from_numpy(spec).unsqueeze(0).to(device)
        
        rr = extract_rr(ecg_seg)
        if len(rr) == 0:
            rr = np.ones(60) * 600
        rr = rr[:60]
        if len(rr) < 60:
            rr = np.pad(rr, (0, 60-len(rr)), constant_values=rr[-1] if len(rr)>0 else 600)
        rr_t = torch.from_numpy(rr.reshape(1,60,1).astype(np.float32)).to(device)
        
        spo2_f = spo2_features(spo2_arr)
        spo2_t = torch.from_numpy(spo2_f.reshape(1,9).astype(np.float32)).to(device)
        
        out = model(spec=spec_t, rr=rr_t, spo2=spo2_t)
        probs = torch.softmax(out, dim=1)[0]
        conf = float(probs[1].cpu().item())
    
    pred = 'APNEA DETECTED' if conf > 0.5 else 'NORMAL'
    ahi = round(conf * 40, 1)
    if ahi < 5:
        sev = 'Normal'
    elif ahi < 15:
        sev = 'Mild'
    elif ahi < 30:
        sev = 'Moderate'
    else:
        sev = 'Severe'
    
    print('\n'+'-'*60)
    print('PREDICTION RESULT')
    print('-'*60)
    print(f'Prediction: {pred}')
    print(f'Confidence: {conf:.2%}')
    print(f'AHI Proxy: {ahi} events/hour')
    print(f'Severity: {sev}')
    print('-'*60)
    print('\n[MODEL] CNN-BiLSTM + Attention with Spectrogram + RR + SpO2 fusion')
    print('[DATA] Using trained weights from weights/fusion_best.pth')
    print('='*60)
    
    result = {
        'prediction': pred,
        'confidence': conf,
        'ahi_proxy': ahi,
        'severity': sev,
        'input_file': args.input
    }
    with open('prediction_result.json', 'w') as f:
        json.dump(result, f, indent=2)
    print('\nResult saved to prediction_result.json')

if __name__=='__main__':
    main()
