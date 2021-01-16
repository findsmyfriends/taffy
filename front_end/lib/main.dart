import 'package:flutter/material.dart';
import 'package:flutter_restapi/adddatawidget.dart';
import 'dart:async';
import 'package:flutter_restapi/models/cases.dart';
import 'package:flutter_restapi/services/api_service.dart';
import 'package:flutter_restapi/caseslist.dart';

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
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ApiService api = ApiService();
  List<Cases> casesList;

  @override
  Widget build(BuildContext context) {
    if (casesList == null) {
      casesList = List<Cases>();
    }

    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: new Container(
        child: new Center(
            child: new FutureBuilder(
          future: loadList(),
          builder: (context, snapshot) {
            return casesList.length > 0
                ? new CasesList(cases: casesList)
                : new Center(
                    child: new Text('No data found, tap plus button to add!',
                        style: Theme.of(context).textTheme.title));
          },
        )),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _navigateToAddScreen(context);
        },
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  Future loadList() {
    Future<List<Cases>> futureCases = api.getCases();
    futureCases.then((casesList) {
      setState(() {
        this.casesList = casesList;
      });
    });
    return futureCases;
  }

  _navigateToAddScreen(BuildContext context) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AddDataWidget()),
    );
  }
}
