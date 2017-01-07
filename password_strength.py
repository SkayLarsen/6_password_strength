from getpass import getpass
import re
import os.path


def check_blacklist(password, path):
    if not path:
        return None
    if not os.path.exists(path):
        print("Невозможно открыть файл, чёрный список не будет использован.")
        return None
    with open(path, 'r') as bl_file:
        blacklist = bl_file.readlines()
    return password in blacklist


def get_length_score(password):
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
    patterns = ['\+?[0-9\-()\s]+',  # номер телефона
                '\w+\@\w+\.\w+',  # e-mail
                '([0-9]{1,4}[\\/.\s]?){3}'  # дата
                ]
    password_score = 1

    if any(char.isdigit() for char in password):
        password_score += 2
    if any(char.isupper() for char in password):
        password_score += 2
    if any(char in password for char in symbols):
        password_score += 2

    for pattern in patterns:
        pattern = re.compile(pattern)
        if pattern.fullmatch(password):
            password_score -= 3

    password_score += get_length_score(password)
    if password_score < 1:
        password_score = 1

    return password_score


if __name__ == '__main__':
    passwd = getpass("Введите пароль для проверки: ")
    blacklist_path = input("Введите путь к файлу с черным списком паролей (если файла нет, просто нажмите Enter): ")
    if not check_blacklist(passwd, blacklist_path):
        print("Оценка сложности пароля: ", get_password_strength(passwd))
    else:
        print("Пароль в чёрном списке!")
