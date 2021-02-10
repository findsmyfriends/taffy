import 'package:adobe_xd/adobe_xd.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'package:carousel_slider/carousel_slider.dart';
import 'package:frontend/curve_container_account.dart';
import 'package:frontend/settings/setting_main_page.dart';

import 'addmedia/select_source.dart';
import 'editprofile/edit_profile_,main.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'models/member_models.dart';

final Widget placeholder = Container(color: Colors.grey);

List<T> map<T>(List list, Function handler) {
  List<T> result = [];
  for (var i = 0; i < list.length; i++) {
    result.add(handler(i, list[i]));
  }

  return result;
}

class AccountTab extends StatefulWidget {
  AccountTab({Key key, this.username, this.url}) : super(key: key);
  final String url;
  final String username;

  @override
  _AccountTabState createState() => _AccountTabState();
}

class _AccountTabState extends State<AccountTab> {
  String username = '';
  String password = '';
  int _current = 0;

  Widget swipeWidgetText(image, upperText, [lowerText = ""]) {
    return Container(
      child: Column(
        children: <Widget>[
          SizedBox(
            height: 8,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Image.asset(
                image,
                width: 26,
                height: 26,
              ),
              SizedBox(
                width: 6,
              ),
              Text(
                upperText,
                style: TextStyle(
                  color: Colors.black,
                  fontWeight: FontWeight.bold,
                  fontSize: 18,
                ),
              ),
            ],
          ),
          SizedBox(
            height: 8,
          ),
          Text(
            lowerText,
            style: TextStyle(
              color: Colors.grey,
            ),
          )
        ],
      ),
    );
  }

  void getToServer() async {
    var url = widget.url;
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    // print('Response status:=============> ${response.statusCode}');
    // print('Response body:===============> ${response.body}');
    print(".......................................................");
    // List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    // print('utf8decode: $result');
    print('---convert to list of members---');

    // List<Members> members =
    //     result.map<Members>((data) => Members.fromMap(data)).toList();

    // members.forEach((members) => print(members.toString()));
    // print("type =======> ${members.runtimeType}");
  }

  @override
  Widget build(BuildContext context) {
    List<Widget> yoFuck = [
      swipeWidgetText("assets/location_icon.png", "Swipe around the world!",
          "Passport to anywhere with tinder plus"),
      swipeWidgetText("assets/key_icon.png", "Control your profile",
          "Limit what other can see with Tinder Plus! "),
      swipeWidgetText("assets/reload_icon.png", "I mean't to swipe right",
          "Get Unlimited rewrad with tinder plus"),
      swipeWidgetText("assets/heart_icon.png", "Increase your Chances",
          "Get Unlimited likes with tinder plus! "),
    ];
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        color: Colors.grey[50],
        child: Column(
          children: <Widget>[
            Stack(
              alignment: Alignment.center,
              children: <Widget>[
                Pinned.fromSize(
                    bounds: Rect.fromLTWH(0, 0, 0, 0), size: Size(340, 70))
                // Container(),
              ],
            ),
            ClipPath(
              clipper: CurvedBottomClipper(),
              child: Container(
                decoration: BoxDecoration(
                  // shape: BoxShape.rectangle,
                  // borderRadius: BorderRadius.only(
                  //   bottomLeft: Radius.circular(120),
                  //   bottomRight: Radius.circular(120),
                  // ),
                  color: Colors.pink[600],
                ),
                width: MediaQuery.of(context).size.width,
                height: 250,
                child: Column(
                  children: <Widget>[
                    SizedBox(
                      height: 70,
                    ),
                    CircleAvatar(
                      foregroundColor: Colors.black,
                      radius: 80,
                      child: CircleAvatar(
                        radius: 75,
                        backgroundImage: NetworkImage(".url"),
                      ),
                      backgroundColor: Colors.white,
                    ),
                    SizedBox(
                      height: 20,
                    ),
                  ],
                ),
              ),
            ),
            // Container(
            //   alignment: Alignment.center,
            //   child: Text("data"),
            // ),
            SizedBox(
              height: 12,
            ),
            Text(
              "Atul Chaudhary, 21",
              style: TextStyle(
                color: Colors.black,
                fontSize: 30,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                GestureDetector(
                  onTap: () {
                    getToServer();
                    // Navigator.push(context,
                    //     MaterialPageRoute(builder: (context) => SettingPage()));
                  },
                  child: Container(
                    child: Column(
                      children: <Widget>[
                        Container(
                          padding: EdgeInsets.all(20),
                          decoration: BoxDecoration(
                            color: Colors.grey[200],
                            shape: BoxShape.circle,
                            //borderRadius: BorderRadius.only()
                          ),
                          child: Image.asset(
                            "assets/setting_icon.png",
                            width: 30,
                            height: 30,
                          ),
                        ),
                        SizedBox(
                          height: 6,
                        ),
                        Text(
                          "SETTINGS",
                          style: TextStyle(
                              color: Colors.grey, fontWeight: FontWeight.bold),
                        )
                      ],
                    ),
                  ),
                ),
                Container(
                  margin: EdgeInsets.fromLTRB(0, 36, 0, 0),
                  child: Column(
                    children: <Widget>[
                      GestureDetector(
                        onTap: () {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => SelectSource()));
                        },
                        child: Container(
                          padding: EdgeInsets.all(20),
                          decoration: BoxDecoration(
                            color: Colors.grey[200],
                            shape: BoxShape.circle,
                            gradient: LinearGradient(
                              colors: [
                                Color.fromRGBO(253, 41, 123, 1),
                                Color.fromRGBO(255, 88, 100, 1),
                                Color.fromRGBO(255, 101, 91, 1)
                              ],
                              begin: Alignment.bottomLeft,
                              end: Alignment.topRight,
                            ),
                            //borderRadius: BorderRadius.only()
                          ),
                          child: Image.asset(
                            "assets/camera_icon.png",
                            width: 30,
                            height: 30,
                          ),
                        ),
                      ),
                      SizedBox(
                        height: 6,
                      ),
                      Text(
                        "ADD MEDIA",
                        style: TextStyle(
                            color: Colors.grey, fontWeight: FontWeight.bold),
                      )
                    ],
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => EditProfile()));
                  },
                  child: Container(
                    child: Column(
                      children: <Widget>[
                        Container(
                          padding: EdgeInsets.all(20),
                          decoration: BoxDecoration(
                            color: Colors.grey[200],
                            shape: BoxShape.circle,
                            //borderRadius: BorderRadius.only()
                          ),
                          child: Image.asset(
                            "assets/edit_icon.png",
                            width: 30,
                            height: 30,
                          ),
                        ),
                        SizedBox(
                          height: 6,
                        ),
                        Text(
                          "EDIT INFO",
                          style: TextStyle(
                              color: Colors.grey, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(
              height: 40,
            ),
            Container(
              child: Column(
                children: [
                  CarouselSlider(
                    height: 70,
                    items: yoFuck,
                    autoPlay: true,
                    enlargeCenterPage: true,
                    //aspectRatio: 2.0,
                    onPageChanged: (index) {
                      setState(() {
                        _current = index;
                      });
                    },
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: map<Widget>(
                      yoFuck,
                      (index, url) {
                        return Container(
                          width: 8.0,
                          height: 8.0,
                          margin: EdgeInsets.symmetric(
                              vertical: 10.0, horizontal: 2.0),
                          decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              color: _current == index
                                  ? Colors.blue
                                  : Color.fromRGBO(0, 0, 0, 0.2)),
                        );
                      },
                    ),
                  ),
                ],
              ),
            ),
            SizedBox(
              height: 8,
            ),
            Container(
              decoration: BoxDecoration(
                  color: Colors.yellow[50],
                  //shape: BoxShape.rectangle,
                  borderRadius: BorderRadius.circular(16)),
              padding: EdgeInsets.fromLTRB(26, 16, 26, 16),
              child: Text(
                "MY TAFFY GOLDS",
                style: TextStyle(
                    color: Colors.red[400],
                    fontWeight: FontWeight.bold,
                    fontSize: 18),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
