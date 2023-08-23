true_login = "sky@gmail.com"

true_password = "12345"

user_login = str(input())
user_password = str(input())

if user_login == true_login and user_password == true_password:
    print("Вы вошли в систему")
else:
    print('Неверный логин или пароль.')