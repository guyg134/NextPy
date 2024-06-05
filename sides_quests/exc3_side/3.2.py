def read_file(file_name):
    """
    read the content of a file
    :param file_name: the name of the file to read
    """
    print("__CONTENT_START__")
    # try to open the file
    try:
        file = open(file_name, "r")
    # if the file does not exist print __NO_SUCH_FILE__
    except FileNotFoundError:
        print(f"__NO_SUCH_FILE__")
    # if the file exists print the content of the file
    else:
        print(file.read())
        # close the file
        file.close()
    # finally print __CONTENT_END__
    finally:
        print("__CONTENT_END__")
    

def main():
    """
    print one file that does not exist and one that does
    """
    read_file("no_file.txt")
    print("*" * 25)
    read_file("sides_quests\\exc3_side\\names.txt")


if __name__ == "__main__":
    main()