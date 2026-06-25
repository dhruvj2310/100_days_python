print("🏝️ Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# First Choice
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":

    # Second Choice
    choice2 = input("You've come to a lake. There is an island in the middle.\n"
                    "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if choice2 == "wait":

        # Third Choice
        choice3 = input("You arrive at the island unharmed.\n"
                        "There is a house with 3 doors.\n"
                        "One red, one blue, and one yellow.\n"
                        "Which colour do you choose? ").lower()

        if choice3 == "yellow":
            print("🎉 You found the treasure! You Win!")
        elif choice3 == "red":
            print("🔥 Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("🐺 Eaten by beasts. Game Over.")
        else:
            print("❌ Game Over.")

    else:
        print("🐟 Attacked by trout. Game Over.")

else:
    print("🕳️ Fall into a hole. Game Over.")