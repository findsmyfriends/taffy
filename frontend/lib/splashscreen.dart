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
            margin: EdgeInsets.fromLTRB(0, 300, 0, 0),
            alignment: Alignment.center,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Image.asset(
                  // assets\images\logo1.png
                  "assets/images/logo1.png",
                  width: 120,
                  height: 160,
                  fit: BoxFit.fill,
                ),
                SizedBox(
                  width: 3,
                ),
                Text(
                  "Taffy \nDatting\nApp",
                  style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 40,
                      letterSpacing: 3.0),
                )
              ],
            ),
          ),

          // return Scaffold(
          //   backgroundColor: const Color(0xFFFF2E7E),

          //   body: new Stack(
          //     children: <Widget>[
          //       Container(
          //           alignment: Alignment.center,
          //           child: new Image.asset("assets/images/logo.png")),
          //       Container(
          //         height: 20,
          //         alignment: Alignment.bottomCenter,
          //         child: const Text(
          //           "Taffy version 0.0.1SE",
          //           style: TextStyle(
          //               // fontWeight: FontWeight.bold,
          //               fontSize: 15.0,
          //               color: Colors.white),
          //         ),
          //       ),
          //       SizedBox(
          //         height: 20,
          //       )
          //     ],
          //     alignment: Alignment.bottomLeft,
          //     clipBehavior: Clip.hardEdge,
          //   ),
          // );
        ]),
      ),
    );
  }
}
