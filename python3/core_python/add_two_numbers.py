

def main():
    num1 = 0
    num2 = 0

    try:
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
    except Exception as e:
        print("Invalid input.", e)
        exit(0)

    sum = num1 + num2

    print(f"Addition of {num1} and {num2} is {sum}")


if __name__ == '__main__':
    main()
