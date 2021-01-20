import 'dart:async';

import 'package:flutter/material.dart';

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    startTime();
  }

  startTime() async {
    var _duration = new Duration(seconds: 4);
    return new Timer(_duration, navigationPage);
  }

  void navigationPage() {
    Navigator.of(context).pushReplacementNamed('/welcomepage');
  }

  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFF2E7E),
      body: new Stack(
        children: <Widget>[
          Container(
              alignment: Alignment.center,
              child: new Image.asset("assets/images/logo.png")),
          Container(
            alignment: Alignment.bottomCenter,
            child: const Text(
              "Taffy version 0.0.1SE",
              style: TextStyle(
                  // fontWeight: FontWeight.bold,
                  fontSize: 15.0,
                  color: Colors.white),
            ),
          ),
        ],
        alignment: Alignment.bottomLeft,
        clipBehavior: Clip.hardEdge,
      ),
    );
  }
}
