#Write a Python program to count the number 4 in a given list.


def main():
    l1 = [12, 74, 4, 23, 32, 4, 55, 40, 4]

    key = 4

    count = 0

    for i in l1:
        if i == key:
            count += 1

    print(f'Key : {key} accuracy is : {count}')



if __name__ == '__main__':
    main()