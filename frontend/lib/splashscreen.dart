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
    var _duration = new Duration(seconds: 6);
    return new Timer(_duration, navigationPage);
  }

  void navigationPage() {
    //Navigator.of(context).pushReplacementNamed('/welcomepage');
    Navigator.of(context).pushReplacementNamed('/welcomepage');
  }

  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Color.fromRGBO(253, 41, 123, 1),
              Color.fromRGBO(255, 88, 100, 1),
              Color.fromRGBO(255, 101, 91, 1)
            ],
            begin: Alignment.bottomLeft,
            end: Alignment.topRight,
          ),
        ),
        child: Column(children: <Widget>[
          Container(
            margin: EdgeInsets.fromLTRB(0, 300, 23, 0),
            alignment: Alignment.center,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Image.asset(
                  "assets/images/logo1.png",
                  width: 120,
                  height: 160,
                  fit: BoxFit.cover,
                ),
                SizedBox(
                  width: 3,
                ),
                Text(
                  "Taffy \nApp",
                  style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 40,
                      letterSpacing: 3.0),
                )
              ],
            ),
          ),
        ]),
      ),
    );
  }
}
