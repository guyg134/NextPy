def get_fibo():
    """
    This function returns a generator for fibonachi seriesq
    """
    # First two numbers of fibonachi series
    a, b = 0, 1 
    while True:
        # Return the next number in the series
        yield a
        # Update the series
        a, b = b, a + b
    
    


def main():
    # Test the function
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == "__main__":
    main()