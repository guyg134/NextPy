from animals.animal import Animal
from animals.dog import Dog
from animals.cat import Cat
from animals.skunk import Skunk
from animals.unicorn import Unicorn
from animals.dragon import Dragon


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
