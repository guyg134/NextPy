from itertools import combinations

def getHundred(money):
    """
    all possible combinations of money to get 100 dollars
    :param money: list of money
    """
    count = 0 # count of combinations
    seen = set()  # hash set to store combinations already seen

    # get all combinations of length 1 to len(money)
    for i in range(1, len(money) + 1):
        # get all combinations of length i
        for comb in combinations(money, i):
            # check if sum of combination is 100
            if sum(comb) == 100:
                # Use a sorted tuple to ensure identical combinations are hashed the same
                if tuple(sorted(comb)) not in seen:
                    # add combination to hash set and print
                    seen.add(tuple(sorted(comb)))
                    print(comb)
                    count += 1

    print("Total combinations: ", count)


def main():
    money = [ 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1 ]
    getHundred(money)


if __name__ == "__main__":
    main()