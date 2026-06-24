print("Welcome to the rollercoaster! 🎢")

height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age?: "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 17:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photos = input("Do you want photos taken of you?(answwer y for Yes and n for No): ")

    if wants_photos == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, You have to grow taller before you can ride the rollercoaster!")