# my favorite animal is a Dog so I will create a class for it
class Dog:
    # class variable to keep track of the number of animals
    count_animals = 0 
    def __init__(self, name = "Octavio"):
        """
        Initializes a Dog object with a name and age of 0.
        if no name is given, the default name is Octavio
        """
        # set the name of the Dog as the given name
        self._name = name
        # set the age of the Dog to 0
        self._age = 0
        # add one to the count of animals
        Dog.count_animals += 1 

    def birthday(self):
        """
        Increments the age of the Dog by one.
        """
        self._age += 1
    
    def get_age(self):
        """"
        Returns the age of the Dog.
        """
        return self._age
    
    def get_name(self):
        """
        Returns the name of the Dog.
        """
        return self._name
    
    def set_name(self, name):
        """
        Sets the name of the Dog to the given name.
        """
        self._name = name

def main():
    """
    Create two Dog objects and test the birthday method.
    Print the age of the first Dog and the second Dog.
    """
    # create two Dog objects
    first_dog = Dog("Walter")
    second_dog = Dog()

    # increment the age of the first Dog
    first_dog.birthday() 
    # print the age of the first and second Dog
    print("Age of first Dog:", first_dog.get_age())
    print("Age of second Dog:", second_dog.get_age())

    # change the name of the first Dog and print
    first_dog.set_name("Walter White")
    print("Name of first Dog:", first_dog.get_age())

    # number of Dogs created
    print("Number of Dogs", Dog.count_animals) 

if __name__ == '__main__':
    main()