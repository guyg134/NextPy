import file1
import file2

def main():
    # Greeeting card
    card1 = file1.GreetingCard("Rami", "Doni")
    print(card1.greeting_msg())
    print('*' * 20)
    # Birthday card
    card2 = file2.BirthdayCard(25)
    print(card2.greeting_msg())

if __name__ == "__main__":
    main()