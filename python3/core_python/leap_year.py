

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def main():
    year = 0
    try:
        year = int(input("Enter a year: "))
    except ValueError as e:
        print("Invalid Input.", e)
        exit(0)
    except Exception as e:
        print("Something wrong.", e)
        exit(0)

    if is_leap_year(year):
        print("Leap Year")
    else:
        print("Not a Leap Year")


if __name__ == '__main__':
    main()
