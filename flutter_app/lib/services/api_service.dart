import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://10.0.2.2:5000';

  Future<Map<String, dynamic>> predictWatchSim() async {
    final res = await http.post(
      Uri.parse('$baseUrl/predict'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'mode': 'watch_sim', 'simulated': true}),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> calibrate() async {
    final res = await http.post(Uri.parse('$baseUrl/calibrate'));
    return jsonDecode(res.body);
  }
}
