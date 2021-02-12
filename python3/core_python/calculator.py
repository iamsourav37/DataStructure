
def calculator(a,b):
    sum = a + b
    sub = a - b
    mult = a * b
    expo = a**b
    if b != 0:
        div = a/b
        integer_division = a//b
        rem = a % b
    else:
        div = "ZERO division is not possible"
        rem = "ZERO division is not possible"
        integer_division = "ZERO division is not possible"

    print("Addition : ", sum)
    print("Substraction : ", sub)
    print("Multiplication : ", mult)
    print("Division : ", div)
    print("Exponent : ", expo)
    print("Modulas : ", rem)
    print("integer_division : ", integer_division)


def main():
    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))
    calculator(number1, number2)



if __name__ == "__main__":
    main()