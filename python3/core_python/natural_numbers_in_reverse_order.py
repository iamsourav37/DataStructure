# Print first N natural numbers in reverse order


def main():
    n = int(input("Enter N: "))

    tmp = n

    while tmp > 0:
        print(tmp, end=' ')
        tmp -= 1
    print()
    # another way

    for i in range(n, 0, -1):
        print(i, end=' ')


if __name__ == '__main__':
    main()

