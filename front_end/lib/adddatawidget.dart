import 'package:flutter/material.dart';
import 'package:flutter_restapi/services/api_service.dart';
import 'models/cases.dart';

enum Gender { male, female }
enum Testes { male, female }

// enum Status { positive, dead, recovered }

class AddDataWidget extends StatefulWidget {
  AddDataWidget();

  @override
  _AddDataWidgetState createState() => _AddDataWidgetState();
}

class _AddDataWidgetState extends State<AddDataWidget> {
  _AddDataWidgetState();

  // id: json['_id'] as String,
  // name: json['name'] as String,
  // gender: json['gender'] as String,
  // age: json['age'] as int,
  // address: json['address'] as String,
  // city: json['city'] as String,
  // country: json['country'] as String,
  // status: json['status'] as String,
  // updated: json['updated'] as String,

  // id: json['id'] as int,
  // username: json['username'] as String,
  // email: json['email'] as String,
  // password: json['password'] as String,
  // first_name: json['first_name'] as String,
  // last_name: json['last_name'] as String,
  // birthday: json['birthday'] as String,
  // age: json['age'] as int,
  // profileurl: json['profileurl'] as String,
  // discription: json['discription'] as String,
  // characterneed: json['characterneed'] as int,
  // values: json['values'] as int,
  // created_at: json['created_at'] as String,
  // updated_at: json['updated_at'] as String,
  // dayofbirth: json['dayofbirth'] as String,
  // rasi: json['rasi'] as String,
  // bloodtype: json['bloodtype'] as String,
  // naksus: json['naksus'] as String,
  // gender: json['gender'] as String,
  // testes: json['testes'] as String

  final ApiService api = ApiService();
  final _addFormKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _firstnameController = TextEditingController();
  final _lastnameController = TextEditingController();
  final _birthdayController = TextEditingController();
  final _ageController = TextEditingController();
  // final _profileurlController = TextEditingController();
  // final _discriptionController = TextEditingController();
  // final _characterneedController = TextEditingController();
  // final _valuesController = TextEditingController();
  // final _created_atController = TextEditingController();
  // final _updated_atController = TextEditingController();
  // final _dayofbirthController = TextEditingController();
  // final _rasiController = TextEditingController();
  // final _bloodtypeController = TextEditingController();
  // final _naksusController = TextEditingController();
  // final _genderController = TextEditingController();
  String gender = 'male';
  Gender _gender = Gender.male;
  // String testes = 'male';
  // Testes _testes = Testes.male;
  // final _testesController = TextEditingController();

  // final _addressController = TextEditingController();
  // final _cityController = TextEditingController();
  // final _countryController = TextEditingController();
  // String status = 'positive';
  // Status _status = Status.positive;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Cases'),
      ),
      body: Form(
        key: _addFormKey,
        child: SingleChildScrollView(
          child: Container(
            padding: EdgeInsets.all(20.0),
            child: Card(
                child: Container(
                    padding: EdgeInsets.all(10.0),
                    width: 440,
                    child: Column(
                      children: <Widget>[
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Full Name'),
                              TextFormField(
                                controller: _usernameController,
                                decoration: const InputDecoration(
                                  hintText: 'User Name',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter full name';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Email'),
                              TextFormField(
                                controller: _emailController,
                                decoration: const InputDecoration(
                                  hintText: 'Email',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter@email.com';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Password'),
                              TextFormField(
                                controller: _passwordController,
                                decoration: const InputDecoration(
                                  hintText: 'password',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter password';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Gender'),
                              ListTile(
                                title: const Text('Male'),
                                leading: Radio(
                                  value: Gender.male,
                                  groupValue: _gender,
                                  onChanged: (Gender value) {
                                    setState(() {
                                      _gender = value;
                                      gender = 'male';
                                    });
                                  },
                                ),
                              ),
                              ListTile(
                                title: const Text('Female'),
                                leading: Radio(
                                  value: Gender.female,
                                  groupValue: _gender,
                                  onChanged: (Gender value) {
                                    setState(() {
                                      _gender = value;
                                      gender = 'female';
                                    });
                                  },
                                ),
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Age'),
                              TextFormField(
                                controller: _ageController,
                                decoration: const InputDecoration(
                                  hintText: 'Age',
                                ),
                                keyboardType: TextInputType.number,
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter age';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('First_name'),
                              TextFormField(
                                controller: _firstnameController,
                                decoration: const InputDecoration(
                                  hintText: 'first name',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter Firstname';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Last_name'),
                              TextFormField(
                                controller: _lastnameController,
                                decoration: const InputDecoration(
                                  hintText: 'last name',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter Lastname';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        // Container(
                        //   margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                        //   child: Column(
                        //     children: <Widget>[
                        //       Text('City'),
                        //       TextFormField(
                        //         controller: _cityController,
                        //         decoration: const InputDecoration(
                        //           hintText: 'City',
                        //         ),
                        //         validator: (value) {
                        //           if (value.isEmpty) {
                        //             return 'Please enter city';
                        //           }
                        //           return null;
                        //         },
                        //         onChanged: (value) {},
                        //       ),
                        //     ],
                        //   ),
                        // ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              Text('Birthday'),
                              TextFormField(
                                controller: _birthdayController,
                                decoration: const InputDecoration(
                                  hintText: 'birthday',
                                ),
                                validator: (value) {
                                  if (value.isEmpty) {
                                    return 'Please enter Birthday';
                                  }
                                  return null;
                                },
                                onChanged: (value) {},
                              ),
                            ],
                          ),
                        ),
                        // Container(
                        //   margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                        //   child: Column(
                        //     children: <Widget>[
                        //       Text('Status'),
                        //       ListTile(
                        //         title: const Text('Positive'),
                        //         leading: Radio(
                        //           value: Status.positive,
                        //           groupValue: _status,
                        //           onChanged: (Status value) {
                        //             setState(() {
                        //               _status = value;
                        //               status = 'positive';
                        //             });
                        //           },
                        //         ),
                        //       ),
                        //       ListTile(
                        //         title: const Text('Dead'),
                        //         leading: Radio(
                        //           value: Status.dead,
                        //           groupValue: _status,
                        //           onChanged: (Status value) {
                        //             setState(() {
                        //               _status = value;
                        //               status = 'dead';
                        //             });
                        //           },
                        //         ),
                        //       ),
                        //       ListTile(
                        //         title: const Text('Recovered'),
                        //         leading: Radio(
                        //           value: Status.recovered,
                        //           groupValue: _status,
                        //           onChanged: (Status value) {
                        //             setState(() {
                        //               _status = value;
                        //               status = 'recovered';
                        //             });
                        //           },
                        //         ),
                        //       ),
                        //     ],
                        //   ),
                        // ),
                        Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                          child: Column(
                            children: <Widget>[
                              RaisedButton(
                                splashColor: Colors.red,
                                onPressed: () {
                                  if (_addFormKey.currentState.validate()) {
                                    _addFormKey.currentState.save();
                                    api.createCase(Cases(
                                      username: _usernameController.text,
                                      email: _emailController.text,
                                      password: _passwordController.text,
                                      firstname: _firstnameController.text,
                                      lastname: _lastnameController.text,
                                      gender: gender,
                                      birthday: _birthdayController.text,
                                      age: int.parse(_ageController.text),
                                      // address: _addressController.text,
                                      // city: _cityController.text,
                                      // country: _countryController.text,
                                      // status: status
                                    ));

                                    Navigator.pop(context);
                                  }
                                },
                                child: Text('Save',
                                    style: TextStyle(color: Colors.white)),
                                color: Colors.blue,
                              )
                            ],
                          ),
                        ),
                      ],
                    ))),
          ),
        ),
      ),
    );
  }
}
