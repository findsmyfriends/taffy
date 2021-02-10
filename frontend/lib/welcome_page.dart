import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:frontend/registerpages.dart';
import 'login_username.dart';
// import 'tinderHomePage.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  bool isFacebookLoginIn = false;
  String errorMessage = '';
  String successMessage = '';

  void navigationRegisterPages() {
    Navigator.of(context).pushReplacement(new MaterialPageRoute(
        settings: const RouteSettings(name: '/HomePage'),
        builder: (context) => new RegisterPages()));
  }

  void navigationLoginPages() {
    Navigator.of(context).pushReplacement(new MaterialPageRoute(
        settings: const RouteSettings(name: '/HomePage'),
        builder: (context) => new LoginUsername()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        // width: double.infinity,
        // height: double.infinity,
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
        child: Column(
          children: <Widget>[
            Container(
              margin: EdgeInsets.fromLTRB(0, 180, 25, 0),
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
                    "Taffy \nApp",
                    style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 40,
                        letterSpacing: 2.0),
                  )
                ],
              ),
            ),
            Expanded(
              child: Align(
                alignment: Alignment.bottomCenter,
                child: Container(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: <Widget>[
                      Text(
                        "มาเป้นส่วนหนึ่งในแอปพลิเคชันของเราสิ !",
                        style: TextStyle(
                            color: Colors.white, fontWeight: FontWeight.bold),
                      ),
                      SizedBox(
                        height: 4,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Text(
                            "Terms of service",
                            style: TextStyle(
                                color: Colors.white,
                                decoration: TextDecoration.underline,
                                fontWeight: FontWeight.bold),
                          ),
                          Text(
                            " and ",
                            style: TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold),
                          ),
                          Text(
                            "Privacy Policy",
                            style: TextStyle(
                                color: Colors.white,
                                decoration: TextDecoration.underline,
                                fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      GestureDetector(
                        onTap: () {
                          print("LoginPages ========> go");
                          navigationLoginPages();

                          // Navigator.push(
                          //     context,
                          //     MaterialPageRoute(
                          //         builder: (context) => LoginUsername()));
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
                            "LOG ON APPLICATIONS",
                            style: TextStyle(
                                color: Colors.black,
                                fontWeight: FontWeight.bold,
                                fontSize: 16),
                          ),
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          print("Register ========> ");
                          navigationRegisterPages();
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => RegisterPages()));
                        },
                        child: Container(
                          width: double.infinity,
                          alignment: Alignment.center,
                          padding: EdgeInsets.fromLTRB(0, 16, 0, 16),
                          margin: EdgeInsets.fromLTRB(24, 0, 24, 10),
                          decoration: BoxDecoration(
                              color: Colors.transparent,
                              border: Border.all(color: Colors.white, width: 2),
                              borderRadius: BorderRadius.circular(26)),
                          child: Text(
                            "RIGISTER ON APPLICATIONS",
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
                      Text(
                        "Trouble logging in?",
                        style: TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                            decoration: TextDecoration.underline),
                      ),
                      SizedBox(
                        height: 16,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Text(
                            "We don't post anything on Facebook",
                            style: TextStyle(
                              color: Colors.white,
                            ),
                          ),
                          SizedBox(
                            width: 3,
                          ),
                          Icon(
                            Icons.keyboard_arrow_down,
                            color: Colors.white,
                          ),
                        ],
                      ),
                      SizedBox(
                        height: 8,
                      ),
                    ],
                  ),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
