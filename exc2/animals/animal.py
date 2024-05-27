class Animal:
    zoo_name = "Hayaton"
    #initialize the name and hunger of the animal
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    
    def get_name(self):
        """Return the name of the animal"""
        return self._name
    
    def is_hungry(self):
        """Return True if the animal is hungry"""
        #return True if the hunger is greater than 0
        return self._hunger > 0
    
    def feed(self):
        """Feed the animal"""
        #decrement the hunger by 1, but not less than 0
        self._hunger = max(0, self._hunger - 1)

    def talk(self):
        """Talk method for the animal"""
        pass

    def __str__(self):
        """Return the string representation of the animal"""
        #return the type name and the name of the animal
        return type(self).__name__ + " " + self._name
    