def send_invitation(name, age):
    """
    send an invitation to a person if they are at least 18 years old
    else print an error message using raise and except
    :param name: the name of the person
    :param age: the age of the person
    """
    try:
        if int(age) < 18:
            raise ValueError("You should be at least 18 years old to send an invitation")
        else:
            print("You should send an invite to " + name)
    
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Invitation sending process completed")

def main():
    send_invitation("John", 16)
    send_invitation("Jane", 23)


if __name__ == "__main__":
    main()