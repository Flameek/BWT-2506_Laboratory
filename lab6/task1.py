class User_Account():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password # Приватный атрибут для хранения паролей
        
    def set_password(self, new_password):
        self.__password = new_password
    
    def check_password(self, check_passw):
        return self.__password == check_passw
    
username = input("Введите имя пользователя: ")
email = input("Введите электронную почту: ")
password = input("Введите пароль: ")

user = User_Account(username, email, password)

password_to_check = input("Введите пароль для проверки: ")
if user.check_password(password_to_check):
    print("Пароль верный!")
else:
    print("Пароль неверный!")

new_password = input("Введите новый пароль: ")
user.set_password(new_password)

password_to_check = input("Введите новый пароль для проверки: ")
if user.check_password(password_to_check):
    print("Пароль верный!")
else:
    print("Пароль неверный!")
    
print(user.username)
print(user.__password)

        