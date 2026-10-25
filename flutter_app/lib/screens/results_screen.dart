import 'package:flutter/material.dart';
import '../widgets/gradient_card.dart';

class ResultsScreen extends StatelessWidget {
  final Map<String, dynamic>? data;
  const ResultsScreen({super.key, this.data});

  @override
  Widget build(BuildContext context) {
    final d = data ?? {'prediction': 'APNEA SUSPECTED', 'confidence': 0.87, 'ahi_proxy': 12.4, 'severity': 'Moderate'};
    return Scaffold(
      backgroundColor: const Color(0xFF0B1026),
      appBar: AppBar(backgroundColor: Colors.transparent, title: const Text('Results', style: TextStyle(color: Colors.white))),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            GradientCard(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(d['prediction'], style: const TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold)),
              const SizedBox(height: 4),
              Text('Confidence: ${(d['confidence']*100).toStringAsFixed(1)}%', style: const TextStyle(color: Colors.white70)),
            ])),
            const SizedBox(height: 12),
            Row(children: [
              Expanded(child: _stat('AHI-Proxy', '${d['ahi_proxy']} /hr')),
              Expanded(child: _stat('Severity', d['severity'])),
            ]),
            const SizedBox(height: 12),
            const Card(color: Color(0xFF151A2C), child: ListTile(title: Text('Fusion', style: TextStyle(color: Colors.white)), subtitle: Text('Spectrogram + RR + SpO2 (embeddings)', style: TextStyle(color: Colors.white54)))),
            const Spacer(),
            const Text('SIMULATED WATCH DATA - For Academic Demo Only', textAlign: TextAlign.center, style: TextStyle(color: Colors.redAccent)),
          ],
        ),
      ),
    );
  }

  Widget _stat(String k, String v) {
    return Card(color: const Color(0xFF151A2C), child: Padding(padding: const EdgeInsets.all(12), child: Column(children: [Text(v, style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold)), Text(k, style: const TextStyle(color: Colors.white54))])));
  }
}
