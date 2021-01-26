// import 'dart:convert';
// import 'package:frontend/models/member_models.dart';
// import 'package:http/http.dart' as http;
// import 'dart:async';

// import 'package:http/http.dart';

// class ApiService {
//   final String apiUrl = "https://taffy.pythonanywhere.com/api/member/";

//   Future<List<Members>> getMembers() async {
//     Response res = await get(apiUrl);

//     if (res.statusCode == 200) {
//       List<dynamic> body = jsonDecode(res.body);
//       List<Members> members =
//           body.map((dynamic item) => Members.fromJson(item)).toList();
//       return members;
//     } else {
//       throw "Failed to load memberss list";
//     }
//   }

//   Future<Members> getCaseById(String id) async {
//     final response = await get('$apiUrl/$id');

//     if (response.statusCode == 200) {
//       return Members.fromJson(json.decode(response.body));
//     } else {
//       throw Exception('Failed to load a case');
//     }
//   }

//   Future<Members> createCase(Members members) async {
//     Map data = {
//       'id': members.id,
//       'username': members.username,
//       'email': members.email,
//       'password': members.password,
//       'firstname': members.firstname,
//       'lastname': members.lastname,
//       'birthday': members.birthday,
//       'age': members.age,
//       'profileurl': members.profileurl,
//       'discription': members.discription,
//       'characterneed': members.characterneed,
//       'values': members.values,
//       'createdat': members.createdat,
//       'updatedat': members.updatedat,
//       'dayofbirth': members.dayofbirth,
//       'rasi': members.rasi,
//       'bloodtype': members.bloodtype,
//       'naksus': members.naksus,
//       'gender': members.gender,
//       'testes': members.testes
//     };

//     final Response response = await post(
//       apiUrl,
//       headers: <String, String>{
//         'Content-Type': 'application/json; charset=UTF-8',
//       },
//       body: jsonEncode(data),
//     );
//     if (response.statusCode == 200) {
//       return Members.fromJson(json.decode(response.body));
//     } else {
//       throw Exception('Failed to post Members');
//     }
//   }

//   Future<Members> updateMembers(String id, Members members) async {
//     Map data = {
//       'id': members.id,
//       'username': members.username,
//       'email': members.email,
//       'password': members.password,
//       'firstname': members.firstname,
//       'lastname': members.lastname,
//       'birthday': members.birthday,
//       'age': members.age,
//       'profileurl': members.profileurl,
//       'discription': members.discription,
//       'characterneed': members.characterneed,
//       'values': members.values,
//       'createdat': members.createdat,
//       'updatedat': members.updatedat,
//       'dayofbirth': members.dayofbirth,
//       'rasi': members.rasi,
//       'bloodtype': members.bloodtype,
//       'naksus': members.naksus,
//       'gender': members.gender,
//       'testes': members.testes
//     };

//     final Response response = await put(
//       '$apiUrl/$id',
//       headers: <String, String>{
//         'Content-Type': 'application/json; charset=UTF-8',
//       },
//       body: jsonEncode(data),
//     );
//     if (response.statusCode == 200) {
//       return Members.fromJson(json.decode(response.body));
//     } else {
//       throw Exception('Failed to update a case');
//     }
//   }

//   Future<void> deleteCase(String id) async {
//     Response res = await delete('$apiUrl/$id');

//     if (res.statusCode == 200) {
//       print("Case deleted");
//     } else {
//       throw "Failed to delete a case.";
//     }
//   }
// }
