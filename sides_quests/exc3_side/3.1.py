# Function that raises StopIteration exception
def raise_stop_iteration():
    raise StopIteration("This is a StopIteration error")

# Function that raises ZeroDivisionError exception
def raise_zero_division_error():
    raise ZeroDivisionError("This is a ZeroDivisionError error")

# Function that raises AssertionError exception
def raise_assertion_error():
    raise AssertionError("This is an AssertionError error")

# Function that raises ImportError exception
def raise_import_error():
    raise ImportError("This is an ImportError error")

# Function that raises KeyError exception
def raise_key_error():
    raise KeyError("This is a KeyError error")

# Function that raises SyntaxError exception
def raise_syntax_error():
    raise SyntaxError("This is a SyntaxError error")

# Function that raises IndentationError exception
def raise_indentation_error():
    raise IndentationError("This is an IndentationError error")

# Function that raises TypeError exception
def raise_type_error():
    raise TypeError("This is a TypeError error")

def main():
    """
    all the functions will raise different errors
    """
    raise_stop_iteration()
    raise_zero_division_error()
    raise_assertion_error()
    raise_import_error()
    raise_key_error()
    raise_syntax_error()
    raise_indentation_error()
    raise_type_error()


if __name__ == "__main__":
    main()