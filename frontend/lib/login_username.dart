import 'package:flutter/material.dart';

import 'package:frontend/models/member_models.dart';
import 'package:frontend/models/user_models.dart';
import 'package:frontend/models/userlogin_models.dart';
import 'package:frontend/myhomepage.dart';
import 'package:frontend/registerpages.dart';

import 'package:http/http.dart' as http;
import 'dart:convert';
import 'account_tab.dart';

// import 'package:firebase_auth/firebase_auth.dart';

class LoginUsername extends StatefulWidget {
  LoginUsername({
    Key key,
    this.id,
    this.username,
    this.password,
  }) : super(key: key);

  final String username;
  final String password;
  final int id;

  @override
  _LoginUsernameState createState() => _LoginUsernameState();
}

class _LoginUsernameState extends State<LoginUsername> {
  GlobalKey<FormState> _key = new GlobalKey();
  bool _validate = false;
  String username, password;
  int id;

  void getToServer() async {
    String token;
    var url = 'https://taffy.pythonanywhere.com/auth/login/';
    var response = await http.post(url, headers: {
      'Content-Type': 'application/json; charset=UTF-8',
      'Accept': 'application/json',
      'Authorization': 'Bearer $token',
    });
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));

    List<Members> members =
        result.map<Members>((data) => Members.fromMap(data)).toList();

    members.forEach((members) => print(members.toString()));

    if (response.statusCode == 200) {
      members.forEach((members) {
        if (members.username == this.username &&
            members.password == this.password) {
          print(
              "username ${members.username} ${members.age} ${members.first_name}");

          Navigator.of(context).pushReplacement(new MaterialPageRoute(
              settings: const RouteSettings(name: '/home'),
              // builder: (context) => new MyHomePage(
              builder: (context) => new AccountTab(
                  username: members.username, url: members.url)));
        } else {
          print("object Errored ${members.first_name}");
          print("username: ${members.url} password: ${members.password} ");
        }
      });
    } else {
      throw Exception('Unable to fetch Memberss from the REST API');
    }
  }

  Future<Token> getToken(UserLogin userLogin) async {
    Map data = {
      'username': userLogin.username,
      'password': userLogin.password,
    };

    final http.Response response = await http.post(
      'https://taffy.pythonanywhere.com/auth/login/',
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(data),
    );
    if (response.statusCode == 200) {
      print("____GET TOKEN RESPOSE____");
      // print(json.decode(response.body).toString());
      Map<String, dynamic> result = json.decode(response.body);
      print(result["access"].toString());
      // var result;
      // return Token.result["access"].toString();
      // result.forEach((key, value) {
      //   // return Token.key;/
      //   print("${key.toString()}: ${value}");
      // });
      // return Token.fromJson(json.decode(response.body));
    } else {
      print(json.decode(response.body).toString());
      throw Exception(json.decode(response.body));
    }
  }

  Future<User> createMember(User user) async {
    Map data = {
      'username': user.username,
      'password': user.password,
    };
    // var body = jsonEncode(data);
    String token;
    var url = 'https://taffy.pythonanywhere.com/auth/login/';
    var response = await http.post(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json',
        'Authorization': 'Bearer $token',
      },
      body: jsonEncode(data),
    );

    if (response.statusCode == 200) {
      // If the server did return a 201 CREATED response,
      // then parse the JSON.
      Map<String, dynamic> result = json.decode(response.body);
      // result.forEach((key, value) => print("${key}:${value}")

      // return text(key, value.toString());
      // );

      UserLogin admin = UserLogin(username: username, password: password);
      Token token = await getToken(admin);
      print("____________${token}____________");

      // print(result["access"]);

      print("response.statusCode :${response.statusCode} ");

      // navigationPage();

      // Navigator.of(context).pushReplacement(new MaterialPageRoute(
      //     settings: const RouteSettings(name: '/home'),
      //     builder: (context) => new MyHomePage()));
      // builder: (context) => new AccountTab()));

      return User.fromJson(json.decode(response.body));
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.
      // final UserLogin admin = UserLogin(username: username, password: password);
      // final Token token = await getToken(admin);
      // print("____________${token}____________");

      print("response.statusCode :${response.statusCode} ");
      print("response.bodyBytes :${response.body} ");

      Map<String, dynamic> result = json.decode(response.body);
      result.forEach((key, value) {
        print("${key = key.toString()}: ${value = value[0]}");
        // return text(key, value.toString());
      });

      // throw Exception('Failed to Add User');
    }
  }

  void navigationPage() {
    Navigator.of(context).pushReplacementNamed('/home');
    // Navigator.of(context).pushReplacement(new MaterialPageRoute(
    //     settings: const RouteSettings(name: '/HomePage'),
    //     builder: (context) => new MyHomePage(
    //           username: username,
    //         )));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        decoration: BoxDecoration(
          color: Colors.white,
        ),
        child: Stack(children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              SafeArea(
                child: GestureDetector(
                  onTap: () {
                    Navigator.pop(context);
                  },
                  child: Container(
                    //color: Colors.grey,
                    margin: EdgeInsets.all(20.0),
                    // child: Icon(
                    //   Icons.arrow_back,
                    //   color: Colors.red[400],
                    // ),
                  ),
                ),
              ),
            ],
          ),
          Container(
            margin: EdgeInsets.fromLTRB(36, 75, 36, 0
                // MediaQuery.of(context).size.height,
                ),
            child: Text(
              "Login Pages",
              textAlign: TextAlign.left,
              style: TextStyle(
                  color: Colors.grey[700],
                  fontSize: 36,
                  fontWeight: FontWeight.bold),
            ),
          ),
          Container(
              margin: EdgeInsets.fromLTRB(
                36,
                120,
                36,
                0,
              ),
              child: ListView(children: <Widget>[
                Container(
                  child: new Form(
                    key: _key,
                    autovalidate: _validate,
                    child: FormUI(),
                  ),
                ),
              ]))
        ]),
      ),
    );
  }

  Widget FormUI() {
    return new Column(
      children: <Widget>[
        new TextFormField(
          decoration: new InputDecoration(
              icon: Icon(Icons.person), hintText: 'Username'),
          maxLength: 150,
          validator: validateUsername,
          onSaved: (String val) {
            username = val;
          },
        ),

        new SizedBox(height: 20.0),
        new TextFormField(
          obscureText: true,
          decoration: new InputDecoration(
              icon: Icon(Icons.vpn_key), hintText: 'Password'),
          // maxLength: 32,
          validator: validatePassword,
          onSaved: (String val) {
            password = val;
          },
        ),

        new SizedBox(height: 20.0),
        // new Text("noty: ${getNoty}"),
        // new RaisedButton(
        //   onPressed: _sendToServer,
        //   // child: new Text('Send'),
        // ),

        GestureDetector(
          onTap: () {
            print("Ontap __");

            _sendToServer();
          },
          child: Container(
            width: double.infinity,
            alignment: Alignment.center,
            padding: EdgeInsets.fromLTRB(0, 16, 0, 16),
            margin: EdgeInsets.fromLTRB(24, 20, 24, 10),
            decoration: BoxDecoration(
                gradient: LinearGradient(
                    colors: [Colors.pinkAccent, Colors.black87],
                    begin: Alignment.centerLeft,
                    end: Alignment.centerRight),
                borderRadius: BorderRadius.circular(26)),
            child: Text(
              "Login",
              style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 16),
            ),
          ),
        ),
        SizedBox(
          height: 16,
        ),
        // Text(
        //   "Trouble logging in?",
        //   style: TextStyle(
        //       color: Colors.black,
        //       fontWeight: FontWeight.bold,
        //       decoration: TextDecoration.underline),
        // ),
        SizedBox(
          height: 16,
        ),
        SafeArea(
          child: GestureDetector(
            onTap: () {
              print("Register ========> ");
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => RegisterPages()));
            },
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Icon(
                  Icons.keyboard_arrow_down,
                  color: Colors.black,
                ),
                Text(
                  "หากยังไม่มีบัญชี สามารถสมัครได้ที่นี่",
                  style: TextStyle(
                      color: Colors.black,
                      fontWeight: FontWeight.bold,
                      decoration: TextDecoration.underline),
                ),
                SizedBox(
                  width: 3,
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }

  String validateName(String value) {
    String patttern = r'(^[a-zA-Z ]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Username is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Username must be a-z and A-Z";
    }
    return null;
  }

  String validateMobile(String value) {
    String patttern = r'(^[0-9]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Mobile is Required";
    } else if (value.length != 10) {
      return "Mobile number must 10 digits";
    } else if (!regExp.hasMatch(value)) {
      return "Mobile Number must be digits";
    }
    return null;
  }

  String validatePassword(String value) {
    String patttern = r'(^[0-9 a-zA-Z]*$)';
    RegExp regExp = new RegExp(patttern);
    if (value.length == 0) {
      return "Password is Required";
    } else if (value.length < 8) {
      return "Password must 8 digits";
    } else if (!regExp.hasMatch(value)) {
      return "Password must be digits";
    }
    return null;
  }

  String validateEmail(String value) {
    String pattern =
        r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
    RegExp regExp = new RegExp(pattern);
    if (value.length == 0) {
      return "Email is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Invalid Email";
    } else {
      return null;
    }
  }

  String validateUsername(String value) {
    String pattern = r'^(^[a-zA-Z @/./+/-/_ ]*$)';
    RegExp regExp = new RegExp(pattern);
    if (value.length == 0) {
      return "Username is Required";
    } else if (!regExp.hasMatch(value)) {
      return "Invalid Username";
    } else {
      return null;
    }
  }

  _sendToServer() {
    if (_key.currentState.validate()) {
      // No any error in validation
      _key.currentState.save();

      createMember(User(
        username: username,
        password: password,
      ));
      // print("Mobile $mobile");
      print("Username $username");

      print("password $password");
    } else {
      // validation error
      setState(() {
        _validate = true;
        // print("ID $id");
        print("object validation error");
      });
    }
  }
}
