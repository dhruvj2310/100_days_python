import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("🃁🂡🂱🃑 LET's PLAY BLACKJACK ! 🃁🂡🂱🃑")

users_cards = random.choices(numbers, k=2)
uc = print(f"Your cards: {users_cards}")

ai_cards = random.choices(numbers)
aic = print(f"Computer's cards: {ai_cards}")

game_over = False

while not game_over:
    new_card = input("type 'y' to get a new card, 'n' to pass: ").lower()

    if new_card == "n":
        ai_card = random.choice(numbers)
        ai_cards.append(ai_card)

        print(f"Your cards: {users_cards}")
        print(f"Computer's cards: {ai_cards}")

    elif new_card == "y":
        ai_card = random.choice(numbers)
        ai_cards.append(ai_card)

        users_card = random.choice(numbers)
        users_cards.append(users_card)

        print(f"Your cards: {users_cards}")
        print(f"Computer's cards: {ai_cards}")

    user_points = sum(users_cards)
    ai_points = sum(ai_cards)

    if user_points < 21:
        if user_points > ai_points:
            print("You Win! 🎉")
            
        else: 
            print("You Lose! Better luck next time.")
    else:
        print("You Lose! Better luck next time.")

    game_over = True
        