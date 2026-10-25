import 'package:flutter/material.dart';

class CalibrateScreen extends StatefulWidget {
  const CalibrateScreen({super.key});

  @override
  State<CalibrateScreen> createState() => _CalibrateScreenState();
}

class _CalibrateScreenState extends State<CalibrateScreen> {
  bool done = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0B1026),
      appBar: AppBar(backgroundColor: Colors.transparent, title: const Text('User Calibration', style: TextStyle(color: Colors.white))),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Card(color: Color(0xFF151A2C), child: Padding(padding: EdgeInsets.all(12), child: Text('Collect/watch HR for baseline. Compute mean -> set personal threshold.', style: TextStyle(color: Colors.white70)))),
            const SizedBox(height: 12),
            ElevatedButton(onPressed: () => setState(() => done = true), child: const Text('Run Calibration (Demo)')),
            if (done) const Text('Calibrated - Baseline set', style: TextStyle(color: Colors.greenAccent)),
          ],
        ),
      ),
    );
  }
}
