import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:frontend/animations/fadeAnimation.dart';
import 'package:frontend/models/member_models.dart';
import 'package:http/http.dart' as http;

class SignIn extends StatefulWidget {
  @override
  _SignInState createState() => _SignInState();
}

class _SignInState extends State<SignIn> {
  @override
  String username = '';
  String password = '';

  void postToServer() async {
    var url = 'https://taffy.pythonanywhere.com/api/member/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    print('Response status: ${response.statusCode}');
    // print('Response body: ${response.body.toString()}');
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    print('utf8decode: $result');
    print('---convert to list of members---');

    List<Members> members =
        result.map<Members>((data) => Members.fromMap(data)).toList();

    members.forEach((members) => print(members.toString()));
  }

  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomPadding: false,
      appBar: AppBar(
        backgroundColor: Color(0xFFFFACDC),
        brightness: Brightness.dark,
        // title: Container(
        //   width: 40,
        //   height: 40,
        //   child: CircleAvatar(
        //     backgroundColor: Colors.transparent,
        //
        //   ),
        //
        // ),
        // centerTitle: true,
        leading: IconButton(
          icon: new Icon(Icons.arrow_back, color: Color(0xFF000000)),
          onPressed: () => Navigator.of(context).pop(),
        ),
      ),
      body: SafeArea(
        child: Container(
          width: double.infinity,
          decoration: BoxDecoration(
            color: Color(0xFFFFFFFF),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Row(mainAxisAlignment: MainAxisAlignment.center,
                  // crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        SizedBox(height: 60),

                        FadeAnimation(
                          1.6,
                          Text(
                            'Sign In',
                            style: TextStyle(
                                color: Color(0xFF000000),
                                fontSize: 35,
                                fontWeight: FontWeight.bold),
                          ),
                        ),

                        SizedBox(
                          height: 10,
                        ),

                        FadeAnimation(
                          1.6,
                          Text(
                            'Welcome To Taffy',
                            style: TextStyle(
                                color: Color(0xFF000000),
                                fontSize: 25,
                                fontWeight: FontWeight.bold),
                          ),
                        ),

                        SizedBox(height: 70),

                        FadeAnimation(
                            1.4,
                            Container(
                              width: 320,
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: <Widget>[
                                  Container(
                                    // padding: EdgeInsets.symmetric(horizontal: 20,vertical: 5),
                                    decoration: BoxDecoration(
                                        border: Border(
                                            bottom: BorderSide(
                                                color: Colors.grey))),
                                    child: TextField(
                                      onChanged: (value) {
                                        this.username = value;
                                        print("Username ==> ${value}");
                                      },
                                      style: TextStyle(
                                          color: Colors.black, fontSize: 20),
                                      decoration: InputDecoration(
                                          icon: Icon(
                                              Icons.person_add_alt_1_outlined),
                                          fillColor: Colors.white,
                                          hintText: "Username",
                                          hintStyle: TextStyle(
                                              color: Colors.grey, fontSize: 14),
                                          border: new UnderlineInputBorder(
                                              borderSide: new BorderSide(
                                                  color: Colors.blueAccent))),
                                    ),
                                  ),
                                  SizedBox(
                                    height: 10,
                                  ),
                                  Container(
                                    // padding: EdgeInsets.symmetric(horizontal: 20,vertical: 5),
                                    decoration: BoxDecoration(
                                        border: Border(
                                            bottom: BorderSide(
                                                color: Colors.grey))),

                                    child: TextField(
                                      onChanged: (value) {
                                        this.password = value;
                                        print("Password ==> ${value}");
                                      },
                                      obscureText: true,
                                      style: TextStyle(
                                          color: Colors.black26, fontSize: 20),
                                      decoration: InputDecoration(
                                          icon: Icon(
                                              Icons.remove_red_eye_outlined),
                                          hintText: "Password",
                                          hintStyle: TextStyle(
                                              color: Colors.grey, fontSize: 14),
                                          border: new UnderlineInputBorder(
                                              borderSide: new BorderSide(
                                                  color: Colors.blueAccent))),
                                    ),
                                  ),
                                ],
                              ),
                            )),

                        SizedBox(
                          height: 60,
                        ),
                        FadeAnimation(
                            1.6,
                            Container(
                                height: 50,
                                width: 320,

                                // margin: EdgeInsets.symmetric(horizontal: 50),
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(20),
                                  gradient: LinearGradient(colors: [
                                    Color(0xFFffb421),
                                    Color(0xFFff7521)
                                  ]),
                                ),
                                child: GestureDetector(
                                  onTap: () {
                                    print(
                                        "Try Login With: ${this.username} ${this.password}");
                                    postToServer();
                                    // Navigator.push(context,MaterialPageRoute(builder: (context) => SignIn()),);
                                  },
                                  child: Center(
                                    child: Text(
                                      "Sign In",
                                      style: TextStyle(
                                          fontSize: 18,
                                          color: Colors.white,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  ),
                                ))),
                        SizedBox(height: 20),
                        FadeAnimation(
                          1.6,
                          Text(
                            'Or sign inn with another\naccount.',
                            style: TextStyle(
                                color: Color(0xFF909093),
                                fontSize: 25,
                                fontWeight: FontWeight.bold),
                          ),
                        ),
                        SizedBox(
                          height: 20,
                        ),
                        FadeAnimation(
                          1.6,
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                child: SvgPicture.asset(
                                  "assets/icons/icons-facebook.svg",
                                  height: 35,
                                  width: 35,
                                ),
                              ),
                              SizedBox(
                                width: 50,
                              ),
                              Container(
                                child: SvgPicture.asset(
                                  "assets/icons/icons-twitter.svg",
                                  height: 35,
                                  width: 35,
                                ),
                              ),
                              SizedBox(
                                width: 50,
                              ),
                              Container(
                                child: SvgPicture.asset(
                                  "assets/icons/icons-google.svg",
                                  height: 35,
                                  width: 35,
                                ),
                              ),
                              SizedBox(
                                width: 50,
                              ),
                            ],
                          ),
                        ),
                        SizedBox(
                          height: 20,
                        ),

                        // SizedBox(height: 30),

                        // FadeAnimation(1.6, Text('Or sign up with another\naccount.',style:
                        // TextStyle(
                        //     color: Color(0xFF909093),
                        //     fontSize: 25,
                        //     fontWeight: FontWeight.bold
                        // ),
                        // ),),
                      ],
                    ),
                  ]),
            ],
          ),
        ),
      ),
    );
  }
}
