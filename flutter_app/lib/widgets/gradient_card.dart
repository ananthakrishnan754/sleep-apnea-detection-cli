import 'package:flutter/material.dart';

class GradientCard extends StatelessWidget {
  final Widget child;
  final List<Color> colors;
  const GradientCard({super.key, required this.child, this.colors = const [Color(0xFF0F1026), Color(0xFF1F3B73)]});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: colors, begin: Alignment.topLeft, end: Alignment.bottomRight),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [BoxShadow(color: Colors.black.withOpacity(0.15), blurRadius: 12, offset: const Offset(0,6))],
      ),
      padding: const EdgeInsets.all(16),
      child: child,
    );
  }
}
