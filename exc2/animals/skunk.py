from .animal import Animal

class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """Talk method for the skunk"""
        print("tsssss")

    def stink(self):
        """Stink method for the skunk"""
        print("Dear lord!")

    def get_stink_count(self):
        """Return the stink count of the skunk"""
        return self._stink_count