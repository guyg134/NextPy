import functools

#Divide by Four
def only_four(number):
    return number % 4 == 0

def four_dividers(number):
    # return a list of numbers that are divisible by 4
    return list(filter(only_four, range(1, number + 1)))


#Double Letters
def two_letters(my_str):
    return my_str * 2

def double_letters(my_str):
    # double each letter in a string
    return ''.join(map(two_letters, my_str))


#print numbers with a coin
def combine_coins(coin, numbers):
    # returns the list with the coin before each number symbol and , between the numbers
    return ', '.join([coin + str(number) for number in numbers])


#Sum of Digits
def add(x, y):
    return x + y

def sum_digits(number):
    # sum all the digits of a number
    # map the number to a string, then map the string to an integer
    return functools.reduce(add, map(int, str(number)))

def main():
    # Test the functions
    print(four_dividers(20))
    print(double_letters('hello'))
    print(combine_coins('$', [1, 2, 3, 4]))
    print(sum_digits(1234))

if __name__ == "__main__":
    main()