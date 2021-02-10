class UserLogin {
  final int id;
  final String username;

  final String password;

  UserLogin({
    this.id,
    this.username,
    this.password,
  });
  factory UserLogin.fromJson(Map<String, dynamic> json) {
    return UserLogin(
      id: json['id'],
      username: json['username'],
      password: json['password'],
    );
  }

  @override
  String toString() {
    return 'ID==>${this.id} UserLoginname==>${this.username}"  )';
  }
}

class Token {
  String token;

  Token({this.token});

  factory Token.fromJson(Map<String, String> json) {
    return Token(token: json['token']);
  }
}
