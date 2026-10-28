# Methodology Explanation - 60-Second ECG Segments & Explainable AI

## 1. How 60-Second ECG Segments Are Extracted

### Data Source
We use the **PhysioNet Apnea-ECG Database v1.0.0** (real clinical recordings). Each recording is a continuous overnight ECG signal sampled at **100 Hz**.

### Segmentation Process
1. **Load Continuous Signal**: Read ECG from WFDB files using `wfdb.rdrecord()` 
2. **Window Creation**: Extract non-overlapping or overlapping windows of **60 seconds** = **6000 samples** (60 × 100 Hz)
3. **Inter-Patient Splitting**: Strict patient-wise split enforced via `splits.json` to prevent data leakage - all windows from a single patient go to only one split (train/val/test)
4. **Annotation Alignment**: Expert annotations (`.apn` files) mark apnea events (A) vs normal (N). Each 60s window is labeled based on majority of annotations within that window
5. **Preprocessing**: Baseline wander removal, noise filtering, and normalization

## 2. How Model Identifies Apnea-Related Events

Our **SleepApneaFusion** model uses three parallel branches:

### Branch 1: Spectrogram Branch (ResNet18)
- **Input**: 60s ECG segment converted to STFT spectrogram
- **STFT Parameters**: `nperseg=512, noverlap=256` 
- **Processing**: Magnitude spectrum → log scaling → normalization → resized to 224×224 → replicated to 3 channels
- **Backbone**: ResNet18 (modified first conv for 1-channel input) extracts spatial features
- **Purpose**: Captures frequency-domain patterns associated with respiratory events

### Branch 2: RR Interval Branch (1D-CNN + BiLSTM + Attention)
- **R-Peak Detection**: `neurokit2.ecg_peaks()` identifies R-peaks
- **RR Extraction**: Compute inter-beat intervals `RR_i = (R_{i+1} - R_i)/fs * 1000` (milliseconds)
- **Outlier Removal**: Median filtering to remove artifacts (±300ms threshold)
- **Feature Engineering**: RR values, differences, and gradients (3 features)
- **CNN**: Extracts local patterns from RR sequence
- **BiLSTM**: Captures long-range temporal dependencies (bidirectional)
- **Attention Mechanism**: Learns to weight important beats/intervals
- **Purpose**: Detects heart rate variability changes characteristic of apnea

### Branch 3: SpO2 Branch (MLP)
- **Features**: min, max, mean, std, variance, skewness, range, count of SpO2 ≤90%, count of SpO2 ≤94%
- **MLP**: Small network processes statistical features
- **Purpose**: Incorporates oxygen desaturation information

### Fusion & Classification
- **Concatenation**: Features from all branches fused (256+256+16 = 528 dims)
- **Classification Head**: FC(528→256) → ReLU → Dropout(0.3) → FC(256→2)
- **Output**: Probability for Normal vs Apnea
- **Decision**: If P(Apnea) > 0.5 → "APNEA DETECTED", else "NORMAL"

## 3. How Explainable AI Justifies Predictions

### Grad-CAM (Gradient-weighted Class Activation Mapping)
- **Applied to**: Spectrogram branch (ResNet18), specifically `layer4[-1]`
- **Method**: Compute gradients of predicted class w.r.t. feature maps, weight by importance
- **Output**: Heatmap highlighting time-frequency regions in spectrogram that influenced decision
- **Interpretation**: Shows which frequency components and time segments drove the classification

### Attention Mechanism (Built-in XAI)
- **Applied to**: BiLSTM in RR branch
- **Method**: Learn attention weights α_t = softmax(W·h_t)
- **Output**: Weight distribution over each RR interval/beat
- **Interpretation**: Identifies which specific heartbeats or RR intervals contributed most to prediction
- **Visualization**: Higher attention weights = more influential beats

### Feature Attribution
- **SpO2 Branch**: Examines which statistical features (desaturations, variability) contributed
- **Multi-branch Fusion**: Model learns optimal combination weights across branches

### Inference Pipeline
1. Segment ECG into 60s windows
2. Extract spectrogram + RR features + SpO2 features
3. Forward pass through all three branches
4. Attention weights extracted from BiLSTM
5. Grad-CAM computed for spectrogram branch
6. Fusion head combines all evidence for final decision
7. Explanation maps highlight specific segments/features responsible

## Key Points
- **Real Data**: Trained on PhysioNet Apnea-ECG (authentic clinical recordings), not synthetic
- **Patient-Aware**: Strict inter-patient splitting prevents overfitting
- **Interpretable**: Both attention (temporal/beat-level) and Grad-CAM (spectro-temporal) provide justifications
- **Multi-Modal**: Combines time-domain (RR), frequency-domain (spectrogram), and physiological (SpO2) information
