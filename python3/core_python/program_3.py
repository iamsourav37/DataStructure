#Write a Python program to test whether a number is within 100 of 1000 or 2000

def main():

    number = 0
    try:
        number = int(input("Enter a number : "))
    except Exception:
        print("Invalid value")
        exit(0)

    if number <=100:
        print("Number is within 100")
    elif number >100 and number<=1000:
        print("Number is within 1000")
    else:
        print("Number is above or equal to 2000")





if __name__ == '__main__':
    main()