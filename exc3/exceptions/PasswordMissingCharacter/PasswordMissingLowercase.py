from .PasswordMissingCharacter import PasswordMissingCharacter

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return f"{super().__str__()} (Lowercase letter)"