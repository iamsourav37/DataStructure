# Print first N natural numbers


def main():
    n = int(input("Enter N : "))

    for i in range(1, n+1):
        print(i, end=" ")


if __name__ == '__main__':
    main()