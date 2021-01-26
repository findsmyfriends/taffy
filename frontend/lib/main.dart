import 'package:flutter/material.dart';

import 'package:frontend/splashscreen.dart';
import 'package:frontend/welcome.dart';

import 'login_page.dart';
import 'myhomepage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.pink,
      ),
      home: SplashScreen(),
      supportedLocales: [
        const Locale('en'), // English
        const Locale('es'), // Spanish
        const Locale('fr'), // French
        const Locale('zh'), // Chinese
        const Locale("th"),
      ],
      routes: <String, WidgetBuilder>{
        '/welcomepage': (BuildContext context) => new LoginPage(),
        '/home': (BuildContext context) => new MyHomePage()
      },
    );
  }
}
