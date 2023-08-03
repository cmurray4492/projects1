"""Common Password Checker"""


def check_password(password: str) -> None:
    """checks user_password against list of common passwords"""
    with open('passwords.txt', 'r', encoding="utf-8") as file:
        common_passwords: list[str] = file.read().splitlines()
        # print(common_passwords)

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: X (#{i})')
            return

    print(f'{password}: (Unique)')


def main():
    """main program functin and entry point"""
    user_password: str = input('Enter a password: ')
    if user_password == "":
        print('You must enter a password!')
        return
    else:
        check_password(user_password)


if __name__ == '__main__':
    main()
