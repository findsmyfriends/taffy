import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/models/member_models.dart';
import 'package:frontend/myhomepage.dart';
// import 'login_google.dart';
import 'dart:async';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'animations/fadeAnimation.dart';
// import 'package:firebase_auth/firebase_auth.dart';

class LoginNumber extends StatefulWidget {
  LoginNumber({Key key, this.username}) : super(key: key);

  final String username;

  // final String _password;

  // LoginNumber(this._username, this._password);
  // LoginNumber(String username);

  @override
  _LoginNumberState createState() => _LoginNumberState();
}

class _LoginNumberState extends State<LoginNumber> {
  final phoneNumberController = TextEditingController();
  bool _validate = false;
  bool _gradientForButton = false;
  String username = '';
  String password = '';
  String ch = '';
  // String countryInfo({code, name}) {
  //   if (code != null && name != null) {
  //     String fullInfo = name + " " + code;
  //     return fullInfo;
  //   }
  //   return "select country code";
  // }

  // bool validateMobile(String value) {
  //   String pattern = r'(^(?:[+0]9)?[0-9]{10,12}$)';
  //   RegExp regExp = new RegExp(pattern);
  //   if (value.length == 0) {
  //     return false;
  //   } else if (!regExp.hasMatch(value)) {
  //     return false;
  //   }
  //   return true;
  // }

  void getToServer() async {
    var url = 'https://taffy.pythonanywhere.com/api/member/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    // print('Response status:=============> ${response.statusCode}');
    // print('Response body:===============> ${response.body}');
    print(".......................................................");
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    print('utf8decode: $result');
    print('---convert to list of members---');

    List<Members> members =
        result.map<Members>((data) => Members.fromMap(data)).toList();

    // List<Members> parseMembers(String responseBody) {
    //   final parsed = json.decode(responseBody).cast<Map<String, dynamic>>();
    //   return parsed.map<Members>((json) => Members.fromMap(json)).toList();
    // }

    members.forEach((members) => print(members.toString()));
    print("type =======> ${members.runtimeType}");
    if (response.statusCode == 200) {
      // print("respose =  ${result.length}");
      members.forEach((members) {
        if (members.username == this.username &&
            members.password == this.password) {
          print(
              "username = ${members.username} ${members.age} ${members.first_name}");
          Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => MyHomePage(username: members.username)),
          );
        } else {
          // MyHomePage(username: members.username);
          // throw Exception('Unable to fetch Memberss from the REST API');
          print("object Errored ${members.first_name}");
          print("username: ${members.username} password: ${members.password} ");
        }
        // print(members.username);
      });
    } else {
      throw Exception('Unable to fetch Memberss from the REST API');
    }
  }

  @override
  void dispose() {
    phoneNumberController.dispose();
    super.dispose();
  }

  Widget headingsForTextField({
    // icon,
    text,
    left,
    top,
    right,
    bottom,
  }) {
    return Container(
      margin: EdgeInsets.fromLTRB(left, top, right, bottom),
      child: Text(
        text,
        style: TextStyle(
          color: Colors.black,
          fontSize: 16,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }

  Widget textField1({icons, hintText, left, right, top, bottom}) {
    return TextField(
      onChanged: (value) {
        this.username = value;
        // members.forEach((members)
        // {}

        print("Username ==> ${this.username}");
      },
      style: TextStyle(
          //color: Colors.white
          ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          icon: icons,
          filled: true,
          fillColor: Colors.white,
          hintText: hintText,
          contentPadding: EdgeInsets.fromLTRB(left, top, right, bottom),
          isDense: true,
          enabledBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white)),
          focusedBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white))
          //border: InputBorder.none
          ),
    );
  }

  Widget PasswordField({icons, hintText, left, right, top, bottom}) {
    return TextField(
      obscureText: true,
      onChanged: (value) {
        this.password = value;
        print("Password ==> ${this.password}");
      },
      style: TextStyle(
          //color: Colors.white
          ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          icon: icons,
          filled: true,
          fillColor: Colors.white,
          hintText: hintText,
          contentPadding: EdgeInsets.fromLTRB(left, top, right, bottom),
          isDense: true,
          enabledBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white)),
          focusedBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white))
          //border: InputBorder.none
          ),
    );
  }

  @override
  Widget build(BuildContext context) {
    LoginNumber username = ModalRoute.of(context).settings.arguments;

    return Scaffold(
      body: Container(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          decoration: BoxDecoration(
            color: Colors.white,
          ),
          child: Stack(
            children: [
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
                        child: Icon(
                          Icons.arrow_back,
                          color: Colors.red[400],
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              Container(
                margin: EdgeInsets.fromLTRB(36, 85, 36, 0
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
                child: ListView(
                  children: <Widget>[
                    // GridViewForPhotos(),

                    headingsForTextField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Username",
                      left: 0.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 4.0,
                    ),

                    textField1(
                      icons: Icon(Icons.person),
                      hintText: "",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(30, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),

                    headingsForTextField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Password",
                      left: 0.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 4.0,
                    ),

                    PasswordField(
                      icons: Icon(Icons.vpn_key),
                      hintText: "",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(30, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    GestureDetector(
                      onTap: () {
                        print(
                            "Try Login With: ${this.username} ${this.password}");
                        getToServer();
                        print("LoginPages ========> go");
                        // Navigator.push(
                        //     context,
                        //     MaterialPageRoute(
                        //         builder: (context) =>
                        //             LoginNumber("IN", "+91")),

                        //             );
                      },
                      child: Container(
                        width: double.infinity,
                        alignment: Alignment.center,
                        padding: EdgeInsets.fromLTRB(0, 16, 0, 16),
                        margin: EdgeInsets.fromLTRB(24, 20, 24, 10),
                        decoration: BoxDecoration(
                            gradient: LinearGradient(
                                colors: [Colors.pinkAccent, Colors.white70],
                                begin: Alignment.centerLeft,
                                end: Alignment.centerRight),
                            borderRadius: BorderRadius.circular(26)),
                        child: Text(
                          "LOGIN ON APPLICATIONS",
                          style: TextStyle(
                              color: Colors.black,
                              fontWeight: FontWeight.bold,
                              fontSize: 16),
                        ),
                      ),
                    ),
                    // Container(
                    //   alignment: Alignment.center,
                    //   margin: EdgeInsets.fromLTRB(0, 15, 0, 0),
                    //   child: FloatingActionButton.extended(
                    //     onPressed: () {
                    //       // Add your onPressed code here!
                    //     },
                    //     label: Text('ลงทะเบียน'),
                    //     icon: Icon(Icons.login_outlined),
                    //     backgroundColor: Colors.pink,
                    //   ),
                    // ),
                  ],
                ),
              )
            ],
          )),
    );
  }
}
