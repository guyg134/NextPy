def parse_ranges(ranges):
    """
    gets a string of ranges and returns a generator of numbers
    using generator expressions
    :param ranges: string of ranges
    """
    # split the ranges by comma
    range_list = (r for r in ranges.split(',')) # first generator
    # iterate over the range_list
    # split the start and end by '-' and convert them to integers
    # return a generator of numbers between start and end
    numbers = (number for r in range_list for number in range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)) # second generator
    return numbers
    


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == "__main__":
    main()