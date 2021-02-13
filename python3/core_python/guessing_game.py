import random


def guessing_game():
    chances = 5
    start = 1
    end = 100
    computer_choose = random.randint(start, end)

    while chances != 0:
        print("You have {} chances left".format(chances))
        print("Choose between {} to {} : ".format(start, end))
        user_choose = int(input())

        if user_choose > end:
            print("Please choose between {} to {}".format(start, end))
            continue
        elif user_choose == computer_choose:
            print("You guess it right, Congratulation You Win !!!")
            return
        elif user_choose < computer_choose:
            print("You choose too low")
        elif user_choose > computer_choose:
            print("You choose too high")
        chances -= 1

    print("You lost !!!")
    print("Computer choose {}".format(computer_choose))



def main():
    while True:
        guessing_game()
        is_continue = input("Want to continue (y/n): ")

        if is_continue[0] == 'y' or is_continue[0] == 'Y':
            continue
        else:
            print("Exit from the game")
            print("Thank You.")
            break


if __name__ == "__main__":
    main()
