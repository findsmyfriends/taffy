import 'package:flutter/material.dart';

import 'package:datetime_picker_formfield/datetime_picker_formfield.dart';
import 'package:frontend/animations/fadeAnimation.dart';

import 'package:intl/intl.dart';

class SignUp extends StatefulWidget {
  @override
  _SignUpState createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  @override
  final format = DateFormat('dd MMM yyyy');
  String _value = 'Birthday';

  Future _selectDate() async {
    DateTime picked = await showDatePicker(
        context: context,
        initialDate: new DateTime.now(),
        firstDate: new DateTime(2021),
        lastDate: new DateTime(2025));
    if (picked != null) setState(() => _value = picked.toString());
  }

  // final format = DateFormat("yyyy-MM-dd");

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
        //     backgroundImage: AssetImage('assets/image/twitter.png'),
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
                        SizedBox(height: 30),
                        FadeAnimation(
                          1.6,
                          Text(
                            'สมัครสมาชิก\nค้นหาเพื่อนรู้ใจ\nค้นหาเพื่อนสัมพันธ์',
                            style: TextStyle(
                                color: Color(0xFF242424),
                                fontSize: 30,
                                fontWeight: FontWeight.bold),
                          ),
                        ),
                        SizedBox(height: 30),
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
                                      style: TextStyle(
                                        fontSize: 20,
                                        color: Colors.black87,
                                      ),
                                      decoration: InputDecoration(
                                          icon: Icon(Icons.email_outlined),
                                          fillColor: Colors.black,
                                          helperStyle: TextStyle(fontSize: 50),
                                          hintText: "Email",
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
                                      // obscureText: true,
                                      style: TextStyle(
                                          color: Colors.black87, fontSize: 20),
                                      decoration: InputDecoration(
                                          icon: Icon(Icons.person_add_outlined),
                                          fillColor: Colors.white,
                                          hintText: "UserName",
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
                                      // obscureText: true,
                                      style: TextStyle(
                                          color: Colors.black87, fontSize: 20),
                                      decoration: InputDecoration(
                                          icon: Icon(Icons.first_page),
                                          fillColor: Colors.white,
                                          hintText: "FirstName",
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
                                      // obscureText: true,
                                      style: TextStyle(
                                          color: Colors.black87, fontSize: 20),
                                      decoration: InputDecoration(
                                          icon: Icon(Icons.last_page),
                                          fillColor: Colors.white,
                                          hintText: "LastName",
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
                                    // padding: EdgeInsets.symmetric(
                                    //     horizontal: 20, vertical: 5),
                                    decoration: BoxDecoration(
                                        border: Border(
                                            bottom: BorderSide(
                                                color: Colors.grey))),

                                    child: Column(
                                      children: <Widget>[
                                        // Text("data"),
                                        DateTimeField(
                                          // obscureText: true,
                                          style: TextStyle(
                                              color: Colors.black,
                                              fontSize: 20),
                                          format: format,
                                          onShowPicker:
                                              (context, currentValue) async {
                                            return showDatePicker(
                                                context: context,
                                                firstDate: DateTime(1900),
                                                initialDate: currentValue ??
                                                    DateTime.now(),
                                                lastDate: DateTime(2100));
                                          },
                                          decoration: InputDecoration(
                                              icon: Icon(Icons
                                                  .calendar_today_outlined),
                                              fillColor: Colors.white,
                                              hintText: _value,
                                              hintStyle: TextStyle(
                                                  color: Colors.grey,
                                                  fontSize: 14),
                                              border: new UnderlineInputBorder(
                                                  borderSide: new BorderSide(
                                                      color:
                                                          Colors.blueAccent))),
                                        ),
                                      ],
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
                                            borderRadius:
                                                BorderRadius.circular(20),
                                            gradient: LinearGradient(colors: [
                                              Color(0xFFFF21AA),
                                              Color(0xFFFF9AD8)
                                            ]),
                                          ),
                                          child: GestureDetector(
                                            onTap: () {
                                              // Navigator.push(context,MaterialPageRoute(builder: (context) => SignUp()),);
                                            },
                                            child: Center(
                                              child: Text(
                                                "Sign Up",
                                                style: TextStyle(
                                                    fontSize: 18,
                                                    color: Colors.white,
                                                    fontWeight:
                                                        FontWeight.bold),
                                              ),
                                            ),
                                          ))),
                                ],
                              ),
                            )),
                        // SizedBox(height: 20),
                        // FadeAnimation(
                        //   1.6,
                        //   Text(
                        //     'Or sign up with another\naccount.',
                        //     style: TextStyle(
                        //         color: Color(0xFF909093),
                        //         fontSize: 25,
                        //         fontWeight: FontWeight.bold),
                        //   ),
                        // ),
                        // SizedBox(
                        //   height: 20,
                        // ),
                        // FadeAnimation(
                        //   1.6,
                        //   Row(
                        //     mainAxisAlignment: MainAxisAlignment.center,
                        //     children: [
                        //       Container(
                        //         child: SvgPicture.asset(
                        //           "assets/icons/icons-facebook.svg",
                        //           height: 35,
                        //           width: 35,
                        //         ),
                        //       ),
                        //       SizedBox(
                        //         width: 50,
                        //       ),
                        //       Container(
                        //         child: SvgPicture.asset(
                        //           "assets/icons/icons-twitter.svg",
                        //           height: 35,
                        //           width: 35,
                        //         ),
                        //       ),
                        //       SizedBox(
                        //         width: 50,
                        //       ),
                        //       Container(
                        //         child: SvgPicture.asset(
                        //           "assets/icons/icons-google.svg",
                        //           height: 35,
                        //           width: 35,
                        //         ),
                        //       ),
                        //       SizedBox(
                        //         width: 50,
                        //       ),
                        //     ],
                        //   ),
                        // ),
                        // SizedBox(
                        //   height: 20,
                        // ),
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
