
# GAME RULES

# 1. ROCK WINS AGAINST SCISSORS
# 2. SCISSORS WINS AGAINST PAPER
# 3. PAPER WINS AGAINST ROCK

import random


def show_name():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")


def numbers_to_strings(number):
    switcher = {
        1: 'Rock',
        2: 'Paper',
        3: 'Scissor'
    }
    return switcher.get(number)


def rock_paper_scissors_game():
    MAX_ROUND = 5
    user_score = 0
    computer_score = 0
    round_no = 1
    while round_no <= MAX_ROUND:
        show_name()
        print("Round No {}/{}".format(round_no, MAX_ROUND))
        user_choice_as_number = int(input("Enter your choice(1,2,3) : "))
        computer_choice_as_number = random.randint(1, 3)

        your_choice = numbers_to_strings(user_choice_as_number)
        computer_choice = numbers_to_strings(computer_choice_as_number)

        # user choose Rock and ...
        if your_choice == "Rock":
            if computer_choice == "Paper":
                print("You choose Rock")
                print("Computer choose Paper")
                computer_score += 1
                print("COMPUTER WIN !")
            elif computer_choice == "Scissor":
                print("You choose Rock")
                print("Computer choose Scissors")
                user_score += 1
                print("YOU WIN !")
            elif your_choice == computer_choice:
                print("You choose Rock")
                print("Computer choose Rock")
                print("ITS A DRAW")
        elif your_choice == "Paper":
            if computer_choice == "Rock":
                print("You choose Paper")
                print("Computer choose Rock")
                user_score += 1
                print("YOU WIN !")
            elif computer_choice == "Scissor":
                print("You choose Paper")
                print("Computer choose Scissors")
                computer_score += 1
                print("COMPUTER WIN !")
            elif your_choice == computer_choice:
                print("You choose Paper")
                print("Computer choose Paper")
                print("ITS A DRAW")
        elif your_choice == "Scissor":
            if computer_choice == "Rock":
                print("You choose Scissor")
                print("Computer choose Rock")
                computer_score += 1
                print("COMPUTER WIN !")
            elif computer_choice == "Paper":
                print("You choose Scissor")
                print("Computer choose Paper")
                user_score += 1
                print("YOU WIN !")
            elif your_choice == computer_choice:
                print("You choose Scissor")
                print("Computer choose Scissor")
                print("ITS A DRAW")
        round_no += 1

    return user_score, computer_score


def main():
    print("Welcome to Rock Paper Scissors Game")

    while True:
        user_score, computer_score = rock_paper_scissors_game()

        print("\nMatch result ")
        if user_score > computer_score:
            print("YOU WIN THE GAME !")
            print(f"Your Score is : {user_score} and Computer Score is {computer_score}.")
        else:
            print("Computer WIN !")
            print(f" Computer Score is {computer_score}, Your Score is : {user_score}")

        play_again = input("Want to play again(yes/no) :")

        if play_again[0] == 'y' or play_again[0] == 'Y':
            continue
        else:
            print("Exit from the game.")
            print("Thank You !!!")
            exit(0)


if __name__ == "__main__":
    main()
