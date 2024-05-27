from .PasswordMissingCharacter import PasswordMissingCharacter

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return f"{super().__str__()} (Special)"