class BigThing:
    def __init__(self, parameter):
        self._parameter = parameter

    def size(self):
        # if parameter is an integer, set the parameter to the integer
        if isinstance(self._parameter, int):
            return self._parameter
        # if parameter is a list, dictionary, or string, set the parameter to the length of the parameter
        elif isinstance(self._parameter, (list, dict, str)):
            return len(self._parameter)
        # if parameter is not an integer, list, dictionary, or string, set the parameter to 0
        else:
            return 0

class BigCat(BigThing):
    def __init__(self, parameter, weight):
        """
        Initializes the BigCat object with a parameter and weight.
        Inherits the parameter handling from BigThing and adds weight management.

        Params:
        parameter: The data to store in the object, can be of any type.
        weight (float): The weight of the cat.
        """
        # Correctly call the parent class's __init__ method
        super().__init__(parameter)  
        # Initialize the weight attribute
        self._weight = weight  

    def size(self):
        """
        Returns the size of the cat based on its weight.
        """
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"
        

def main():
    my_cat = BigCat("mitzy", 22)
    print("Size of my cat:", my_cat.size())
    my_thing = BigThing("Mitzi")
    print("Size:", my_thing.size())


if __name__ == "__main__":
    main()

    