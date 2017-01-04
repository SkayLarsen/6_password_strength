def get_password_strength(password):
    blacklist = ["Password", "Password1", "Welcome1", "P@ssword", "Summer1!", "password",
                 "Fa$hion1", "Hello123", "Welcome123", "123456q@", "P@ssword1"]
    symbols = ".,:;!?@$%^&*()_+-="
    password_score = 1
    password_length = len(password)

    if password in blacklist:
        return "0. Пароль в чёрном списке!"
    if any(char.isdigit() for char in password):
        password_score += 2
    if any(char.isupper() for char in password):
        password_score += 2
    if any(char in password for char in symbols):
        password_score += 2
    if password_length >= 12:
        password_score += 3
    elif password_length >= 10:
        password_score += 2
    elif password_length >= 8:
        password_score += 1

    return password_score


if __name__ == '__main__':
    passwd = input("Введите пароль для проверки: ")
    print("Оценка сложности пароля: ", get_password_strength(passwd))
