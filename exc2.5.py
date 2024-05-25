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
    
class Dog(Animal):
    def talk(self):
        """Talk method for the dog"""
        print("woof woof")
    
    def fetch_stick(self):
        """Fetch stick method for the dog"""
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        """Talk method for the cat"""
        print("meow")

    def chase_laser(self):
        """Chase laser method for the cat"""
        print("Meeeeow")

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

class Unicorn(Animal):
    def talk(self):
        """Talk method for the unicorn"""
        print("Good day, darling")

    def sing(self):
        """Sing method for the unicorn"""
        print("I'm not your toy...")

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

def main():
    #create instances of each animal
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    #create the new instances of the animals
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    #create a list of the animals
    zoo_lst = [dog, cat, skunk, unicorn, dragon, dog2, cat2, skunk2, unicorn2, dragon2]

    #iterate through the list of animals
    for animal in zoo_lst:
        #print the animal if it is hungry
        if animal.is_hungry():
            print(animal)
        #feed the animal until it is not hungry
        while animal.is_hungry():
            animal.feed()
        #call to the talk method
        animal.talk()

        #call to the specific method of each animal
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    #print the zoo name
    print(Animal.zoo_name)

if __name__ == "__main__":
    main()
