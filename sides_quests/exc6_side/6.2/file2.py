import file1

class BirthdayCard(file1.GreetingCard):
    def __init__(self, sender_age=0):
        self._sender_age = sender_age
        super().__init__()
    
    def greeting_msg(self):
        return f"Dear {self._recipient},\n\nHappy Birthday!\nYou are {self._sender_age} years old\n\nBest wishes,\n{self._sender}"