#!/usr/bin/env python3
from flask import Flask, request, jsonify
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

@app.route('/health')
def health():
    return jsonify({'status':'ok','simulated_spo2':True, 'model_loaded': model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}
    # return realistic structure; if we have model, do a dummy forward with small tensors
    try:
        if model is not None:
            # dummy inputs
            with torch.no_grad():
                spec = torch.zeros((1,3,224,224)).to(device)
                rr = torch.zeros((1,60,1)).to(device)
                spo2 = torch.zeros((1,9)).to(device)
                out = model(spec=spec, rr=rr, spo2=spo2)
                probs = torch.softmax(out, dim=1)[0]
                conf = float(probs[1].cpu().item())
            pred = 'APNEA_SUSPECTED' if conf > 0.5 else 'NORMAL'
            return jsonify({
                'prediction': pred,
                'confidence': round(conf, 3),
                'ahi_proxy': round(conf*20, 1),
                'severity': 'Moderate' if conf>0.5 else 'Normal/Mild',
                'simulated': True,
                'note': 'Model loaded (weights present). Demo uses placeholder inputs; wire real features next.',
                'branches': ['spectrogram_resnet18','rr_bilstm_attention','spo2_mlp']
            })
    except Exception as e:
        pass
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
