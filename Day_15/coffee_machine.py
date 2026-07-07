# ---------------------- MENU ---------------------- #

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# -------------------- RESOURCES -------------------- #

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# -------------------- FUNCTIONS -------------------- #

def print_report():
    """Prints the current machine resources."""
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}\n")


def check_resources(drink):
    """
    Returns True if enough ingredients exist.
    Otherwise prints the missing ingredient.
    """
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    """Returns the total money inserted."""

    print("\nPlease insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickles * 0.05
        + pennies * 0.01
    )

    return total


def process_transaction(payment, drink_cost):
    """
    Returns True if payment is accepted.
    Adds profit and returns change if needed.
    """
    global money

    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(payment - drink_cost, 2)

    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    money += drink_cost
    return True


def make_coffee(drink):
    """Deduct ingredients and serve coffee."""

    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink}. Enjoy!\n")


# -------------------- MAIN PROGRAM -------------------- #

machine_on = True

while machine_on:

    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:

        if check_resources(choice):

            payment = process_coins()

            if process_transaction(payment, MENU[choice]["cost"]):
                make_coffee(choice)

    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")