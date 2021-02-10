class User {
  final int id;
  final String username;
  final String email;
  final String password;
  final String password2;
  final String first_name;
  final String last_name;
  User({
    this.id,
    this.username,
    this.email,
    this.password,
    this.password2,
    this.first_name,
    this.last_name,
  });
  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'],
      username: json['username'],
      email: json['email'],
      first_name: json['first_name'],
      last_name: json['last_name'],
      password: json['password'],
      password2: json['password2'],
    );
  }

  @override
  String toString() {
    return 'ID==>${this.id} Username==>${this.username} First_name: ${this.first_name} "last_name:${this.last_name}"  )';
  }
}
