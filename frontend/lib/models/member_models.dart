class Members {
  final String url;
  final String id;
  final String username;
  final String email;
  final String password;
  final String first_name;
  final String last_name;
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
  Members(
      this.url,
      this.id,
      this.username,
      this.email,
      this.password,
      this.first_name,
      this.last_name,
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
      this.testes);

  factory Members.fromMap(Map<String, dynamic> json) {
    return Members(
        json["url"],
        json['id'],
        json['username'],
        json['email'],
        json['password'],
        json['first_name'],
        json['lastname'],
        json['birthday'],
        json['age'],
        json['profileurl'],
        json['discription'],
        json['characterneed'],
        json['values'],
        json['createdat'],
        json['updated_at'],
        json['dayofbirth'],
        json['rasi'],
        json['bloodtype'],
        json['naksus'],
        json['gender'],
        json['testes']);
  }

  @override
  String toString() {
    return 'Username==>${this.username} "Password:${this.password}" First_name: ${this.first_name} (Age:${this.age})';
  }
}
