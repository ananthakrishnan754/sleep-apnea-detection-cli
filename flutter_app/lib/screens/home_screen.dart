import 'package:flutter/material.dart';
import '../widgets/gradient_card.dart';
import '../widgets/status_badge.dart';
import 'calibrate_screen.dart';
import 'demo_screen.dart';
import 'results_screen.dart';
import 'explain_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0B1026),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: const Text('SleepSync - Apnea Detection', style: TextStyle(color: Colors.white)),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            GradientCard(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: const [
                  Text('Explainable AI for Sleep Apnea', style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                  SizedBox(height: 6),
                  Text('ECG + SpO2 Fusion | Dual-View | Personalization | Watch-Sim', style: TextStyle(color: Colors.white70)),
                  SizedBox(height: 10),
                  StatusBadge(text: 'SIMULATED WATCH DATA'),
                ],
              ),
            ),
            const SizedBox(height: 16),
            _actionTile(context, Icons.tune, 'User Calibration', 'Set personal baseline from HR data', const CalibrateScreen()),
            _actionTile(context, Icons.play_arrow, 'Run Demo (Watch Sim)', 'Degraded ECG + simulated SpO2', const DemoScreen()),
            _actionTile(context, Icons.analytics, 'Results & AHI/Severity', 'Prediction with confidence', const ResultsScreen()),
            _actionTile(context, Icons.bubble_chart, 'Explainability', 'Grad-CAM • Attention • LIME', const ExplainScreen()),
            const Spacer(),
            const Text('Prototype for Review - Module by Module', textAlign: TextAlign.center, style: TextStyle(color: Colors.white38)),
          ],
        ),
      ),
    );
  }

  Widget _actionTile(BuildContext context, IconData icon, String title, String sub, Widget screen) {
    return Card(
      color: const Color(0xFF151A2C),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      margin: const EdgeInsets.only(bottom: 10),
      child: ListTile(
        leading: CircleAvatar(backgroundColor: Colors.cyan.withOpacity(0.2), child: Icon(icon, color: Colors.cyanAccent)),
        title: Text(title, style: const TextStyle(color: Colors.white)),
        subtitle: Text(sub, style: const TextStyle(color: Colors.white54)),
        trailing: const Icon(Icons.chevron_right, color: Colors.white38),
        onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => screen)),
      ),
    );
  }
}
