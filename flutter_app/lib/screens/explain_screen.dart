import 'package:flutter/material.dart';

class ExplainScreen extends StatelessWidget {
  const ExplainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0B1026),
      appBar: AppBar(backgroundColor: Colors.transparent, title: const Text('Explainability', style: TextStyle(color: Colors.white))),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: ListView(
          children: const [
            Card(color: Color(0xFF151A2C), child: ListTile(title: Text('Grad-CAM (Spectrogram)', style: TextStyle(color: Colors.white)), subtitle: Text('ResNet18 layer4[-1]', style: TextStyle(color: Colors.white54)))),
            Card(color: Color(0xFF151A2C), child: ListTile(title: Text('Attention Weights (RR)', style: TextStyle(color: Colors.white)), subtitle: Text('BiLSTM + Additive Attention', style: TextStyle(color: Colors.white54)))),
            Card(color: Color(0xFF151A2C), child: ListTile(title: Text('LIME (Fused)', style: TextStyle(color: Colors.white)), subtitle: Text('Wrapper with RR/SpO2 held fixed', style: TextStyle(color: Colors.white54)))),
            Card(color: Color(0xFF151A2C), child: ListTile(title: Text('RR Denoising Autoencoder', style: TextStyle(color: Colors.white)), subtitle: Text('1D U-Net style - reconstruct watch RR', style: TextStyle(color: Colors.white54)))),
          ],
        ),
      ),
    );
  }
}
