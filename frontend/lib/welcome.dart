import 'package:flutter/material.dart';
import 'package:flutter_custom_clippers/flutter_custom_clippers.dart';
import 'package:frontend/signIn.dart';
import 'package:frontend/signUp.dart';

import 'Animation/FadeAnimation.dart';

class WelcomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Container(
            alignment: Alignment.center,
            width: double.infinity,
            // height: double.infinity,
            decoration: BoxDecoration(
              backgroundBlendMode: BlendMode.colorBurn,
              color: Color(0xFFFFFFFF),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        ClipPath(
                          clipper: WaveClipperTwo(),
                          child: Container(
                            width: 411.4,
                            height: 129.0,
                            decoration: BoxDecoration(
                              gradient: LinearGradient(
                                begin: Alignment.centerLeft,
                                end: Alignment.centerRight,
                                colors: [
                                  Color(0xFFFF33B1),
                                  Color(0xFFFF9676),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: 20),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 35),
                      child: FadeAnimation(
                          1.6,
                          Text(
                            'Join a Taffy\nApplications',
                            style: TextStyle(
                                color: Color(0xFFF8007C),
                                fontWeight: FontWeight.bold,
                                fontSize: 55),
                          )),
                    ),
                    SizedBox(height: 20),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 35),
                      child: FadeAnimation(
                          1.6,
                          Text(
                            'A simple , fun , and creative way to \nshare photos , videos , messages\nwith friends and family ',
                            style: TextStyle(
                                color: Color(0xFF292929),
                                fontWeight: FontWeight.bold,
                                fontSize: 18),
                          )),
                    ),
                    SizedBox(height: 120),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 35),
                      child: FadeAnimation(
                          1.6,
                          Container(
                              height: 50,
                              width: 320,

                              // margin: EdgeInsets.symmetric(horizontal: 50),
                              decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(40),
                                  color: Color(0xFF464646)),
                              child: GestureDetector(
                                child: Center(
                                  child: Text(
                                    "Sign Up",
                                    style: TextStyle(
                                        fontSize: 18,
                                        color: Color(0xFFcccccf),
                                        fontWeight: FontWeight.bold),
                                  ),
                                ),
                                onTap: () {
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(builder: (context) {
                                      return SignUp();
                                    }),
                                  );
                                  print("go to Sign UP");
                                },
                              ))),
                    ),
                    SizedBox(
                      height: 30,
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 35),
                      child: FadeAnimation(
                          1.6,
                          Container(
                              height: 50,
                              width: 320,

                              // margin: EdgeInsets.symmetric(horizontal: 50),
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(40),
                                gradient: LinearGradient(colors: [
                                  Color(0xFFFF21AA),
                                  Color(0xFFFF92D2)
                                ]),
                              ),
                              child: GestureDetector(
                                onTap: () {
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => SignIn()),
                                  );
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
                    ),
                    SizedBox(
                      height: 30,
                    ),
                  ],
                ),
              ],
            )),
      ),
    );
  }
}
