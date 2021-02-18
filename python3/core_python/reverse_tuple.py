

def main():
    mytuple = (12, 32, 12, 9, 5, 7)
    l = list(mytuple)
    l.reverse()
    reversed_tuple = tuple(l)
    print(reversed_tuple)


if __name__ == '__main__':
    main()