import 'package:flutter/material.dart';
import 'package:frontend/login_username.dart';
import 'package:http/http.dart' as http;
import 'package:frontend/models/user_models.dart';
import 'dart:convert';

class RegisterPages extends StatefulWidget {
  // final String _Username;
  // final String _Password;

  // RegisterPages(this._Username, this._Password);
  // RegisterPages({Key key, this._Username, this._Password}) : super(key: key);
  @override
  _RegisterPagesState createState() => _RegisterPagesState();
}

class _RegisterPagesState extends State<RegisterPages> {
  // String _Email = '';
  // String _Username = '';
  // String _Firstname = '';
  // String _Lastname = '';
  // String _Password = '';
  // String _Password2 = '';
  final _addFormKey = GlobalKey<FormState>();
  final _EmailController = TextEditingController();
  final _UsernameController = TextEditingController();
  final _FirstnameController = TextEditingController();
  final _LastnameController = TextEditingController();
  final _PasswordController = TextEditingController();
  final _Password2Controller = TextEditingController();

  // final format = DateFormat('dd MMM yyyy');
  // String _value = 'Birthday';
  void navigationPage() {
    Navigator.of(context).pushReplacement(new MaterialPageRoute(
        settings: const RouteSettings(name: '/LoginPage'),
        builder: (context) => new LoginUsername()));
  }

  Future<User> createMember(User user) async {
    Map data = {
      'email': user.email,
      'username': user.username,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'password': user.password,
      'password2': user.password2,
    };
    var url = 'https://taffy.pythonanywhere.com/auth/register/';
    var response = await http.post(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(data),
    );
    if (response.statusCode == 200) {
      // If the server did return a 201 CREATED response,
      // then parse the JSON.
      return User.fromJson(json.decode(response.body));
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.
      throw Exception('Failed to Add User');
    }
  }

  Widget headingsForTextFormField({
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
          fontSize: 20,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }

  Widget EmailField({icons, hintText, left, right, top, bottom}) {
    return TextFormField(
      onChanged: (value) {
        print(value);
      },
      controller: _EmailController,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Email';
        }
        return null;
      },
      style: TextStyle(
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
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

  Widget UsernameField({icons, hintText, left, right, top, bottom}) {
    return TextFormField(
      onChanged: (value) {
        print(value);
      },
      controller: _UsernameController,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Username';
        }
        return null;
      },
      maxLength: 150,
      style: TextStyle(
        fontSize: 18,
        fontWeight: FontWeight.bold,
      ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 10, fontWeight: FontWeight.bold),
          icon: icons,
          filled: true,
          fillColor: Colors.white,
          hintText: hintText,
          contentPadding: EdgeInsets.fromLTRB(16, 16, 0, 0),
          isDense: true,
          enabledBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white)),
          focusedBorder:
              UnderlineInputBorder(borderSide: BorderSide(color: Colors.white))
          //border: InputBorder.none
          ),
    );
  }

  Widget FirstnameField({icons, hintText, left, right, top, bottom}) {
    return TextFormField(
      onChanged: (value) {
        // this.username = value;
        // // members.forEach((members)
        // // {}

        // print("Username ==> ${this.username}");
      },
      controller: _FirstnameController,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Fisrtname';
        }
        return null;
      },
      style: TextStyle(
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
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

  Widget LastnameField({icons, hintText, left, right, top, bottom}) {
    return TextFormField(
      onChanged: (value) {
        // this.username = value;
        // // members.forEach((members)
        // // {}

        // print("Username ==> ${this.username}");
      },
      controller: _LastnameController,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Lastname';
        }
        return null;
      },
      style: TextStyle(
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
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
    return TextFormField(
      obscureText: true,
      style: TextStyle(
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      controller: _PasswordController,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Password';
        }
        return null;
      },
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
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

  Widget Password2Field({icons, hintText, left, right, top, bottom}) {
    return TextFormField(
      obscureText: true,
      style: TextStyle(
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      controller: _Password2Controller,
      validator: (value) {
        if (value.isEmpty) {
          return 'Please enter Password Again';
        }
        return null;
      },
      keyboardType: TextInputType.text,
      decoration: InputDecoration(
          labelStyle: TextStyle(
              color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
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
                    key: _addFormKey,
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
                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Email",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    EmailField(
                      icons: Icon(Icons.email_outlined),
                      hintText: "exemble@email.com",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    Container(),

                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Username",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    UsernameField(
                      icons: Icon(Icons.person_add_alt_1_rounded),
                      hintText:
                          "Letters, digits and @/./+/-/_ only. Required. 150 characters or fewer. \n ",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),

                    Container(
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Firstname",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    FirstnameField(
                      icons: Icon(Icons.first_page),
                      hintText: "",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Lastname",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    LastnameField(
                      icons: Icon(Icons.last_page),
                      hintText: "",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    // headingsForTextFormField(
                    //   // icon:Icon(Icons.ac_unit)

                    //   text: "Birthday",
                    //   left: 0.0,
                    //   top: 16.0,
                    //   right: 16.0,
                    //   bottom: 4.0,
                    // ),

                    // Container(
                    //   margin: EdgeInsets.fromLTRB(0, 0, 0, 0),
                    //   child: Column(
                    //     children: <Widget>[
                    //       // Text("data"),
                    //       DateTimeField(
                    //         // obscureText: true,
                    //         style: TextStyle(color: Colors.black, fontSize: 20),
                    //         format: format,
                    //         onShowPicker: (context, currentValue) async {
                    //           return showDatePicker(
                    //               context: context,
                    //               firstDate: DateTime(1900),
                    //               initialDate: currentValue ?? DateTime.now(),
                    //               lastDate: DateTime(2100));
                    //         },
                    //         decoration: InputDecoration(
                    //           icon: Icon(Icons.calendar_today_outlined),
                    //           fillColor: Colors.white,
                    //           hintText: "01 Jan 1998",
                    //           hintStyle:
                    //               TextStyle(color: Colors.grey, fontSize: 20),
                    //         ),
                    //       ),
                    //     ],
                    //   ),
                    // ),
                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Password",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
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
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    headingsForTextFormField(
                      // icon:Icon(Icons.ac_unit)

                      text: "Password (Agian)",
                      left: 0.0,
                      top: 10.0,
                      right: 16.0,
                      bottom: 0.0,
                    ),
                    Password2Field(
                      icons: Icon(Icons.vpn_key),
                      hintText: "",
                      left: 16.0,
                      top: 16.0,
                      right: 16.0,
                      bottom: 8.0,
                    ),
                    Container(
                      margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                      decoration: BoxDecoration(
                          border:
                              Border(bottom: BorderSide(color: Colors.grey))),
                    ),
                    GestureDetector(
                      onTap: () {
                        // PostRigister();
                        // if (_addFormKey.currentState.validate()) {
                        //   _addFormKey.currentState.save();
                        createMember(User(
                          email: _EmailController.text,
                          username: _UsernameController.text,
                          first_name: _FirstnameController.text,
                          last_name: _LastnameController.text,
                          password2: _Password2Controller.text,
                          password: _PasswordController.text,
                        ));

                        // }
                        print("Goto LoginPage");
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
                          "Register To Taffy",
                          style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              fontSize: 16),
                        ),
                      ),
                    ),
                  ],
                ),
              )
            ],
          )),
    );
  }
}
