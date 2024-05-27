from .PasswordMissingCharacter import PasswordMissingCharacter

class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return f"{super().__str__()} (Uppercase letter)"