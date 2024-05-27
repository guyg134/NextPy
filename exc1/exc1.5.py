def exc1():
    #exc 1 - print the longest name in the file names.txt
    print(max(open('names.txt').read().split(), key=len))
def exc2():
    #exc 2 - print the sum of the lengths of the names in the file names.txt
    print(sum(len(name) for name in open('names.txt').read().split()))
def exc3():
    #exc 3 - print all names in the file names.txt that are the same length as the shortest name
    names_list = sorted(open('names.txt').read().split(), key=len)
    print('\n'.join(name for name in names_list if len(name) == len(names_list[0])))
def exc4():
    #exc 4 - write to a new file name_length.txt that contains one line for each name in the file names.txt, giving the length of each name
    open('name_length.txt', 'w').write('\n'.join(str(len(name)) for name in open('names.txt').read().split()))
def exc5():
    #exc 5 - print all names in the file names.txt that are the same length as the length specified by the user
    length_input = int(input('Enter a length of words: '))
    print('\n'.join(name for name in open('names.txt').read().split() if len(name) == length_input))


def main():
    exc1()
    exc2()
    exc3()
    exc4()
    exc5()
          
if __name__ == "__main__":
    main()