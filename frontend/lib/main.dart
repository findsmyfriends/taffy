import 'package:flutter/material.dart';
import 'package:frontend/login_username.dart';
import 'package:frontend/splashscreen.dart';

import 'welcome_page.dart';
import 'myhomepage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({Key key, this.id, this.username, this.first_name, this.last_name})
      : super(key: key);
  // This widget is the root of your application.
  final String username;
  final int id;
  final first_name;
  final last_name;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.pink,
      ),
      // home: AccountTab(),
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
        '/home': (BuildContext context) => new MyHomePage(
              username: username,
            ),
        '/login': (BuildContext context) => new LoginUsername(
              id: id,
              username: username,
            ),
      },
    );
  }
}
