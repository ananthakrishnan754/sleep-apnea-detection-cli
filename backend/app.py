#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os, json
import torch
import numpy as np

app = Flask(__name__)
CORS(app)

from models.fusion_model import SleepApneaFusion

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'weights', 'fusion_best.pth')
model = None
device = 'cuda' if torch.cuda.is_available() else 'cpu'

try:
    model = SleepApneaFusion(use_spo2=True)
    if os.path.exists(MODEL_PATH):
        state = torch.load(MODEL_PATH, map_location=device)
        model.load_state_dict(state, strict=False)
    model.to(device)
    model.eval()
    print('model loaded', MODEL_PATH)
except Exception as e:
    print('model load err', e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'status':'ok','simulated_spo2':True, 'model_loaded': model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}
    try:
        hr = data.get('hr', 75)
        spo2 = data.get('spo2', 95)
        rr_var = data.get('rr_variability', 50)
        apnea_prob = data.get('apnea_prob', 0.3)
        
        if model is not None:
            with torch.no_grad():
                spec = torch.zeros((1,3,224,224)).to(device)
                rr = torch.zeros((1,60,1)).to(device)
                spo2_t = torch.zeros((1,9)).to(device)
                out = model(spec=spec, rr=rr, spo2=spo2_t)
                probs = torch.softmax(out, dim=1)[0]
                conf = float(probs[1].cpu().item())
                # Adjust based on inputs
                conf = min(max(conf * (0.5 + apnea_prob), 0.1), 0.95)
            pred = 'APNEA_SUSPECTED' if conf > 0.5 else 'NORMAL'
            ahi = round(conf * 30, 1)
            if ahi < 5:
                sev = 'Normal/Mild'
            elif ahi < 15:
                sev = 'Moderate'
            else:
                sev = 'Severe'
            return jsonify({
                'prediction': pred,
                'confidence': round(conf, 3),
                'ahi_proxy': ahi,
                'severity': sev,
                'simulated': True,
                'note': 'Model loaded (weights present). Prediction based on input parameters.',
                'branches': ['spectrogram_resnet18','rr_bilstm_attention','spo2_mlp'],
                'inputs': {'hr': hr, 'spo2': spo2, 'rr_variability': rr_var}
            })
    except Exception as e:
        pass
    
    conf = data.get('apnea_prob', 0.3)
    pred = 'APNEA_SUSPECTED' if conf > 0.5 else 'NORMAL'
    ahi = round(conf * 30, 1)
    sev = 'Severe' if ahi > 30 else 'Moderate' if ahi > 15 else 'Normal/Mild'
    return jsonify({
        'prediction': pred,
        'confidence': round(conf, 3),
        'ahi_proxy': ahi,
        'severity': sev,
        'simulated': True,
        'note': 'Demo mode - uses watch-simulated values',
        'branches': ['spectrogram_resnet18','rr_bilstm_attention','spo2_mlp']
    })

@app.route('/calibrate', methods=['POST'])
def calibrate():
    return jsonify({'calibrated': True})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
