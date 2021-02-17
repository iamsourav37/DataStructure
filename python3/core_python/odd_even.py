
def main():
    num = 0

    try:
        num = int(input("Enter any number : "))
    except ValueError as e:
        print("Invalid input.", e)
        exit(0)
    except Exception as e:
        print("Something wrong.", e)
        exit(0)

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == '__main__':
    main()
