
import sys
import random

# GUESS THE NUMBER: 1, 2, or 3
game_count = 0
player_win = 0


def guess_the_number():
    global game_count
    global player_win

    player_choice = input("\nGuess the number I'm thinking of... 1, 2, or 3: ")

    if player_choice not in ["1", "2", "3"]:
        print("\nPlease choose between 1, 2, or 3\n")
        return guess_the_number()

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    player = int(player_choice)

    print(f"\n\nYou chose {player}")
    print(f"I was thinking about the number {computer}\n")

    if player == computer:
        game_count += 1
        player_win += 1
        winrate = 100 * float(player_win / game_count)
        print(f"You win!\nYour winrate is: {winrate:.2f}%\n\n")
    else:
        game_count += 1
        winrate = 100 * float(player_win / game_count)
        print("Sorry, better luck next time!\n\n")
        print(f"Your winrate is: {winrate:.2f}%\n\n")

    print("Play again?")

    while True:
        play_again = input("\nY for Yes, or \nQ to Quit:\n\n")
        if play_again.lower() not in ["y", "q"]:
            continue
        else:
            break

    if play_again.lower() == "y":
        return guess_the_number()
    else:
        print("\n        🥳 🥳🥳🥳🥳\nThank you for playing!\n")
        sys.exit("👋 👋 🙋‍♂️  BYE BYE  🙋‍♂️ 👋 👋 \n")


guess_the_number()
