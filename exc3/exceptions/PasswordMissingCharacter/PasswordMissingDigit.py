from .PasswordMissingCharacter import PasswordMissingCharacter

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return f"{super().__str__()} (Digit)"