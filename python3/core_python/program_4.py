# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.


def add(n1, n2, n3):
    if n1 == n2 and n2 == n3:
        return (n1 + n2 + n3) * 3
    else:
        return n1 + n2 + n3


def main():

    n1 = 7
    n2 = 7
    n3 = 7

    print(add(n1, n2, n3))





if __name__ == '__main__':
    main()