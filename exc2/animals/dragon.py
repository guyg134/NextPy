from .animal import Animal

class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """Talk method for the dragon"""
        print("Raaaawr")

    def breath_fire(self):
        """Breath fire method for the dragon"""
        print("$@#$#@$")

    def get_color(self):
        """Return the color of the dragon"""
        return self._color