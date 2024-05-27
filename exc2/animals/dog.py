from .animal import Animal

class Dog(Animal):
    def talk(self):
        """Talk method for the dog"""
        print("woof woof")
    
    def fetch_stick(self):
        """Fetch stick method for the dog"""
        print("There you go, sir!")
