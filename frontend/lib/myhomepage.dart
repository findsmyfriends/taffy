import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  MyHomePage({
    Key key,
    this.id,
    this.username,
  }) : super(key: key);
  final int id;
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
      body: new Center(
        child: new Text(
          "${widget.id} \n ${widget.username} ",
          style: TextStyle(fontSize: 30),
        ),
      ),
    );
  }
}
