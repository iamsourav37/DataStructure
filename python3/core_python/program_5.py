#Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.


def main():
    s1 = input("Enter a string : ")

    if s1.startswith("Is"):
        pass
    else:
        s1 = 'Is '.__add__(s1)  # or s1 = "Is " + s1


    print(s1)


if __name__ == '__main__':
    main()
