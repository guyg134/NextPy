import string
from exceptions.UsernameContainsIllegalCharacter import UsernameContainsIllegalCharacter
from exceptions.UsernameTooShort import UsernameTooShort
from exceptions.UsernameTooLong import UsernameTooLong
from exceptions.PasswordMissingCharacter.PasswordMissingLowercase import PasswordMissingLowercase
from exceptions.PasswordMissingCharacter.PasswordMissingUppercase import PasswordMissingUppercase
from exceptions.PasswordMissingCharacter.PasswordMissingDigit import PasswordMissingDigit
from exceptions.PasswordMissingCharacter.PasswordMissingSpecial import PasswordMissingSpecial
from exceptions.PasswordTooShort import PasswordTooShort
from exceptions.PasswordTooLong import PasswordTooLong

class PasswordTooLong(Exception):
    pass

def check_input(username, password):
    # Get the length of the username and password
    username_length = len(username)
    password_length = len(password)

    # Check if username contains illegal characters
    index = find_illegal_character(username)
    # If index is not None, then there is an illegal character in the username
    if index is not None:
        # Raise an exception with the illegal character and the index of the character
        raise UsernameContainsIllegalCharacter(username[index], index)
    # Check if username is too short or too long
    if username_length < 3:
        # Raise an exception if the username is too short
        raise UsernameTooShort()
    # Check if username is too long
    if username_length > 16:
        # Raise an exception if the username is too long
        raise UsernameTooLong()
    # Check if password is too short, too long or missing characters
    if password_length < 8:
        # Raise an exception if the password is too short
        raise PasswordTooShort()
    # Check if password is too long
    if password_length > 40:
        # Raise an exception if the password is too long
        raise PasswordTooLong()
    # Check if password is missing characters
    # Check if password contains at least one lowercase letter
    if not string_contains(password, string.ascii_lowercase):
        raise PasswordMissingLowercase()
    # Check if password contains at least one uppercase letter
    if not string_contains(password, string.ascii_uppercase):
        raise PasswordMissingUppercase()
    # Check if password contains at least one digit
    if not string_contains(password, string.digits):
        raise PasswordMissingDigit()
    # Check if password contains at least one special character
    if not string_contains(password, string.punctuation):
        raise PasswordMissingSpecial()
        

def string_contains(string, characters):
    """Check if a string contains any of the characters in a list of characters
    :param string: The string to check
    :param characters: The characters to check for
    :return: True if the string contains any of the characters, False otherwise"""
    # Iterate over the characters
    for character in characters:
        # Check if the character is in the string
        if character in string:
            return True
    # Return False if none of the characters are in the string
    return False

def find_illegal_character(input):
    """Find the first illegal character in a string
    :param string: The string to check
    :return: The index of the first illegal character, None if no illegal character is found"""
    length = len(input)
    # Iterate over the string
    for index in range(length):
        # Check if the character is not a letter, digit or underscore
        if input[index] != '_' and input[index] not in string.ascii_letters and input[index] not in string.digits:
            return index
    # Return None if no illegal character is found
    return None

def main():
    valid = False
    while not valid:
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            check_input(name, password)
        except Exception as e:
            print(e)
            print("Try again")
        else:
            valid = True
            print("Ok")
    

if __name__ == "__main__":
    main()
