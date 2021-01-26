import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.username}) : super(key: key);
  final String username;

  // final String password;

  // MyHomePage(String username, String password);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text(widget.username),
      ),
      body: new Center(
        child: new Text('Welcome to Home.!'),
      ),
    );
  }
}
