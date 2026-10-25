// Slider value updates
document.getElementById('hrSlider').addEventListener('input', function() {
    document.getElementById('hrValue').textContent = this.value;
});

document.getElementById('spo2Slider').addEventListener('input', function() {
    document.getElementById('spo2Value').textContent = this.value;
});

document.getElementById('rrSlider').addEventListener('input', function() {
    document.getElementById('rrValue').textContent = this.value;
});

document.getElementById('apneaSlider').addEventListener('input', function() {
    document.getElementById('apneaValue').textContent = this.value;
});

// File upload
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const fileList = document.getElementById('fileList');

uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    const files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
});

function handleFiles(files) {
    fileList.innerHTML = '';
    for (let file of files) {
        const div = document.createElement('div');
        div.className = 'alert alert-info py-2 mb-2';
        div.innerHTML = `<i class="fas fa-file"></i> ${file.name} (${(file.size/1024).toFixed(1)} KB)`;
        fileList.appendChild(div);
    }
}

// Predict button
document.getElementById('predictBtn').addEventListener('click', async () => {
    const btn = document.getElementById('predictBtn');
    const resultBody = document.getElementById('resultBody');
    
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Predicting...';
    
    const inputData = {
        hr: parseInt(document.getElementById('hrSlider').value),
        spo2: parseInt(document.getElementById('spo2Slider').value),
        rr_variability: parseInt(document.getElementById('rrSlider').value),
        apnea_prob: parseFloat(document.getElementById('apneaSlider').value)
    };
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(inputData)
        });
        
        const result = await response.json();
        
        resultBody.innerHTML = `
            <div class="text-center">
                <h3 class="mb-3">${result.prediction === 'APNEA_SUSPECTED' ? '<i class="fas fa-exclamation-triangle text-warning"></i>' : '<i class="fas fa-check-circle text-success"></i>'} ${result.prediction}</h3>
                <div class="row text-start">
                    <div class="col-6"><strong>Confidence:</strong></div>
                    <div class="col-6">${(result.confidence*100).toFixed(1)}%</div>
                    <div class="col-6"><strong>AHI Proxy:</strong></div>
                    <div class="col-6">${result.ahi_proxy} events/hr</div>
                    <div class="col-6"><strong>Severity:</strong></div>
                    <div class="col-6">${result.severity}</div>
                </div>
                <hr>
                <small class="text-muted">${result.note}</small>
                <div class="mt-2">
                    <span class="badge bg-warning text-dark">SIMULATED WATCH DATA</span>
                </div>
            </div>
        `;
    } catch (error) {
        resultBody.innerHTML = `
            <div class="alert alert-danger">
                <i class="fas fa-exclamation-circle"></i> Error: ${error.message}
            </div>
        `;
    }
    
    btn.disabled = false;
    btn.innerHTML = '<i class="fas fa-brain"></i> Predict Sleep Apnea';
});
