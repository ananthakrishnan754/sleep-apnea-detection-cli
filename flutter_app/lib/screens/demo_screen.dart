import 'package:flutter/material.dart';
import 'results_screen.dart';

class DemoScreen extends StatefulWidget {
  const DemoScreen({super.key});

  @override
  State<DemoScreen> createState() => _DemoScreenState();
}

class _DemoScreenState extends State<DemoScreen> {
  bool loading = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0B1026),
      appBar: AppBar(backgroundColor: Colors.transparent, title: const Text('Demo - Watch Simulated', style: TextStyle(color: Colors.white))),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Card(color: Color(0xFF151A2C), child: Padding(padding: EdgeInsets.all(12), child: Text('ECG degraded to watch-like + simulated SpO2', style: TextStyle(color: Colors.white70)))),
            const SizedBox(height: 12),
            ElevatedButton(
              onPressed: () async {
                setState(() => loading = true);
                await Future.delayed(const Duration(seconds: 1));
                if (mounted) Navigator.push(context, MaterialPageRoute(builder: (_) => const ResultsScreen()));
                setState(() => loading = false);
              },
              child: Text(loading ? 'Processing...' : 'Run Demo'),
            ),
            const Spacer(),
            const Text('SIMULATED WATCH DATA', textAlign: TextAlign.center, style: TextStyle(color: Colors.redAccent)),
          ],
        ),
      ),
    );
  }
}
