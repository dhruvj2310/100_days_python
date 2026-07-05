import random

LOGO = r"""
 _   _                 _                  _____ _             _
| \ | |               | |                / ____| |           | |
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __| | ___   ___| |__
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | |/ _ \ / __| '_ \
| |\  | |_| | | | | | | |_) |  __/ |    | |__| | | (_) | (__| | | |
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|_|\___/ \___|_| |_|

"""

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def choose_difficulty():
    """Returns number of attempts based on difficulty."""
    while True:
        difficulty = input("Choose difficulty ('easy' or 'hard'): ").lower()

        if difficulty == "easy":
            return EASY_ATTEMPTS
        elif difficulty == "hard":
            return HARD_ATTEMPTS
        else:
            print("❌ Please enter either 'easy' or 'hard'.\n")


def check_guess(guess, answer):
    """Checks the user's guess."""
    if guess > answer:
        print("📈 Too high.")
        return False
    elif guess < answer:
        print("📉 Too low.")
        return False
    else:
        print(f"🎉 Correct! The number was {answer}. You win!")
        return True


def play_game():
    print(LOGO)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    answer = random.randint(1, 100)
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"\nYou have {attempts} attempt(s) remaining.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
            continue

        if check_guess(guess, answer):
            return

        attempts -= 1

        if attempts > 0:
            print("Guess again.")

    print(f"\n💀 You've run out of attempts.")
    print(f"The correct number was {answer}.")


def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("\n👋 Thanks for playing!")
            break

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()