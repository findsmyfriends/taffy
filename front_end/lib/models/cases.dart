class Cases {
  final String id;
  final String username;
  final String email;
  final String password;
  final String firstname;
  final String lastname;
  final String birthday;
  final int age;
  final String profileurl;
  final String discription;
  final int characterneed;
  final int values;
  final String createdat;
  final String updatedat;
  final String dayofbirth;
  final String rasi;
  final String bloodtype;
  final String naksus;
  final String gender;
  final String testes;
  Cases(
      {this.id,
      this.username,
      this.email,
      this.password,
      this.firstname,
      this.lastname,
      this.birthday,
      this.age,
      this.profileurl,
      this.discription,
      this.characterneed,
      this.values,
      this.createdat,
      this.updatedat,
      this.dayofbirth,
      this.rasi,
      this.bloodtype,
      this.naksus,
      this.gender,
      this.testes});

  factory Cases.fromJson(Map<String, dynamic> json) {
    return Cases(
        id: json['id'] as String,
        username: json['username'] as String,
        email: json['email'] as String,
        password: json['password'] as String,
        firstname: json['firstname'] as String,
        lastname: json['lastname'] as String,
        birthday: json['birthday'] as String,
        age: json['age'] as int,
        profileurl: json['profileurl'] as String,
        discription: json['discription'] as String,
        characterneed: json['characterneed'] as int,
        values: json['values'] as int,
        createdat: json['createdat'] as String,
        updatedat: json['updated_at'] as String,
        dayofbirth: json['dayofbirth'] as String,
        rasi: json['rasi'] as String,
        bloodtype: json['bloodtype'] as String,
        naksus: json['naksus'] as String,
        gender: json['gender'] as String,
        testes: json['testes'] as String
        // id: json['_id'] as String,
        // name: json['name'] as String,
        // gender: json['gender'] as String,
        // age: json['age'] as int,
        // address: json['address'] as String,
        // city: json['city'] as String,
        // country: json['country'] as String,
        // status: json['status'] as String,
        // updated: json['updated'] as String,
        );
  }

  @override
  String toString() {
    return 'Trans{id: $id, name: $username, age: $age}';
  }
}
