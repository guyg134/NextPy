
# Numbers in both lists
def intersection(list_1, list_2):
    # return a list of numbers that are in both lists, wont return duplicates
    return list(number for number in set(list_1) if number in set(list_2))

# Funny string
def is_funny(string):
    # return True if the string contains only the letters 'h' and 'a', False otherwise
    return [letter.lower() == 'h' or letter.lower() == 'a' for letter in string] == [True] * len(string)

# Prime number
def is_prime(number):
    # return True if number is prime, False otherwise
    return [number % i == 0 for i in range(2, number)] == [False] * (number - 2)

# Crack the code
def crack_code(password):
    # returns the message before encryption
    return ''.join([chr(ord(letter) + 2) if letter.isalpha() else letter for letter in password])

def main():
    # Test the functions
    print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
    print(is_funny('haha'))
    print(is_prime(7))
    print(crack_code('abc'))

if __name__ == "__main__":
    main()
