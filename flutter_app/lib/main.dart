import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const SleepApneaApp());
}

class SleepApneaApp extends StatelessWidget {
  const SleepApneaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sleep Apnea - Watch Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
