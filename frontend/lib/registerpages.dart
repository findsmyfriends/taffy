import 'package:flutter/material.dart';

import 'dart:async';

import 'package:datetime_picker_formfield/datetime_picker_formfield.dart';
import 'package:frontend/animations/fadeAnimation.dart';
import 'package:frontend/login_number.dart';
import 'package:frontend/login_page.dart';

import 'package:intl/intl.dart';

class RegisterPages extends StatefulWidget {
  // final String _countryCode;
  // final String _countryName;

  // RegisterPages(this._countryCode, this._countryName);

  @override
  _RegisterPagesState createState() => _RegisterPagesState();
}

class _RegisterPagesState extends State<RegisterPages> {
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

  bool _gradientForButton = false;

  bool isSwitched = true;

  Widget smartPhotos() {
    return Container(
      width: MediaQuery.of(context).size.width,
      decoration: BoxDecoration(
        color: Colors.white,
      ),
      padding: EdgeInsets.fromLTRB(16, 8, 16, 8),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          Text(
            "Smart Photos",
            style: TextStyle(
                color: Colors.red[400],
                fontWeight: FontWeight.bold,
                fontSize: 16),
          ),
          Switch(
            value: isSwitched,
            onChanged: (value) {
              setState(() {
                isSwitched = value;
              });
            },
            activeTrackColor: Colors.red[100],
            activeColor: Colors.red[400],
          ),
        ],
      ),
    );
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

  Widget textField({icons, hintText, left, right, top, bottom}) {
    return TextField(
      maxLength: 500,
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

  Widget textField1({icons, hintText, left, right, top, bottom}) {
    return TextField(
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

  Widget build(BuildContext context) {
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
                  "Register Pages",
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

                      text: "Email",
                      left: 0.0,
                      top: 0.0,
                      right: 16.0,
                      bottom: 4.0,
                    ),

                    textField1(
                      icons: Icon(Icons.email_outlined),
                      hintText: "exemble@email.com",
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

                      text: "Firstname",
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

                      text: "Lastname",
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

                      text: "Birthday",
                      left: 0.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 4.0,
                    ),

                    Container(
                      margin: EdgeInsets.fromLTRB(0, 0, 0, 0),
                      child: Column(
                        children: <Widget>[
                          // Text("data"),
                          DateTimeField(
                            // obscureText: true,
                            style: TextStyle(color: Colors.black, fontSize: 20),
                            format: format,
                            onShowPicker: (context, currentValue) async {
                              return showDatePicker(
                                  context: context,
                                  firstDate: DateTime(1900),
                                  initialDate: currentValue ?? DateTime.now(),
                                  lastDate: DateTime(2100));
                            },
                            decoration: InputDecoration(
                              icon: Icon(Icons.calendar_today_outlined),
                              fillColor: Colors.white,
                              hintText: "01 Jan 1998",
                              hintStyle:
                                  TextStyle(color: Colors.grey, fontSize: 20),
                            ),
                          ),
                        ],
                      ),
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
                        print("LoginPages ========> go");
                        Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) =>
                                    LoginNumber(username: "IN")));
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
