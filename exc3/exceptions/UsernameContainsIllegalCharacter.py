class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, index):
        self.message = "Username contains illegal character: " + illegal_character + " at index " + str(index) + "."

    def __str__(self):
        return self.message