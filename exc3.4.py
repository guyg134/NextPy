import string

class UsernameContainsIllegalCharacter(Exception):
    pass
class UsernameTooShort(Exception):
    pass
class UsernameTooLong(Exception):
    pass
class PasswordMissingCharacter(Exception):
    pass
class PasswordTooShort(Exception):
    pass
class PasswordTooLong(Exception):
    pass

def check_input(username, password):
    username_length = len(username)
    password_length = len(password)
    username = username.replace("_", "") 
    if not username.isalnum():
        raise UsernameContainsIllegalCharacter("Username must contain only alphanumeric characters")
    if username_length < 3:
        raise UsernameTooShort("Username must be at least 3 characters long")
    if username_length > 16:
        raise UsernameTooLong("Username must be at most 16 characters long")
    if not string_contains(password, string.punctuation) or not string_contains(password, string.ascii_lowercase) \
        or not string_contains(password, string.ascii_uppercase) or not string_contains(password, string.digits):
        raise PasswordMissingCharacter("Password must contain only alphanumeric characters")
    if password_length < 8:
        raise PasswordTooShort("Password must be at least 6 characters long")
    if password_length > 40:
        raise PasswordTooLong("Password must be at most 40 characters long")

def string_contains(string, characters):
    for character in characters:
        if character in string:
            return True
    return False

def main():
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        check_input(name, password)
    except Exception as e:
        print(e)
    else:
        print("Ok")

if __name__ == "__main__":
    main()
