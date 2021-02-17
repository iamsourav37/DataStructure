
def add_it_up(n):
    if isinstance(n, int):
        result = n*(n+1)/2
        return int(result)
    else:
        return 0


def better_approach(num):
    try:
        return sum(range(num+1))
    except Exception:
        return 0


def main():
    result = add_it_up(20)
    print(f"Sum of first 20 numbers is : {result}")

    print(f"Sum of first 10 is : {better_approach(10)}")
    print(f"Exception : {add_it_up('ERROR')}")
    print(f"Exception : {better_approach('ERROR')}")


if __name__ == '__main__':
    main()

