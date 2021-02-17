# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

def way_one(num, count):
    result = 0
    while count > 0:
        result = 10 * result + num
        count -= 1
    return result


def another_way(num, count):
    result = str(num) * count

    return int(result)


def main():
    n = 0
    try:
        n = int(input("Enter a digit: "))
    except Exception:
        print("Invalid input")
        exit(0)

    result = n + way_one(n, 2) + way_one(n, 3)
    print(f"n + nn+ nnn = {result}")

    print(f"another mehtod result : {another_way(n, 1) + another_way(n, 2) + another_way(n, 3)}")


if __name__ == '__main__':
    main()


