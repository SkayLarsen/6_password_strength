def check_blacklist(password):
    blacklist = ["Password", "Password1", "Welcome1", "P@ssword", "Summer1!", "password",
                 "Fa$hion1", "Hello123", "Welcome123", "123456q@", "P@ssword1"]
    return password in blacklist


def get_lenght_score(password):
    password_length = len(password)
    if password_length >= 12:
        return 3
    elif password_length >= 10:
        return 2
    elif password_length >= 8:
        return 1
    return 0


def get_password_strength(password):
    symbols = ".,:;!?@$%^&*()_+-="
    password_score = 1

    if any(char.isdigit() for char in password):
        password_score += 2
    if any(char.isupper() for char in password):
        password_score += 2
    if any(char in password for char in symbols):
        password_score += 2

    password_score += get_lenght_score(password)

    return password_score


if __name__ == '__main__':
    passwd = input("Введите пароль для проверки: ")
    if not check_blacklist(passwd):
        print("Оценка сложности пароля: ", get_password_strength(passwd))
    else:
        print("Пароль в чёрном списке!")
