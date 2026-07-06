import random
import os

people_list = [
    {"name": "Cristiano Ronaldo", "followers": 680000000},
    {"name": "Lionel Messi", "followers": 507000000},
    {"name": "Selena Gomez", "followers": 419000000},
    {"name": "Kylie Jenner", "followers": 392000000},
    {"name": "Dwayne Johnson", "followers": 394000000},
    {"name": "Ariana Grande", "followers": 375000000},
    {"name": "Kim Kardashian", "followers": 357000000},
    {"name": "Beyonce", "followers": 311000000},
    {"name": "Khloe Kardashian", "followers": 302000000},
    {"name": "Justin Bieber", "followers": 294000000},
    {"name": "Kendall Jenner", "followers": 287000000},
    {"name": "Taylor Swift", "followers": 281000000},
    {"name": "Virat Kohli", "followers": 282000000},
    {"name": "Jennifer Lopez", "followers": 248000000},
    {"name": "Neymar Jr", "followers": 231000000},
    {"name": "Nicki Minaj", "followers": 225000000},
    {"name": "Kourtney Kardashian", "followers": 218000000},
    {"name": "Miley Cyrus", "followers": 213000000},
    {"name": "Katy Perry", "followers": 203000000},
    {"name": "Zendaya", "followers": 178000000},
    {"name": "Kevin Hart", "followers": 177000000},
    {"name": "Cardi B", "followers": 163000000},
    {"name": "LeBron James", "followers": 160000000},
    {"name": "Demi Lovato", "followers": 153000000},
    {"name": "Rihanna", "followers": 149000000},
    {"name": "Chris Brown", "followers": 145000000},
    {"name": "Drake", "followers": 143000000},
    {"name": "Shakira", "followers": 142000000},
    {"name": "Billie Eilish", "followers": 124000000},
    {"name": "Gal Gadot", "followers": 108000000},
    {"name": "Priyanka Chopra", "followers": 92000000},
    {"name": "Shraddha Kapoor", "followers": 95000000},
    {"name": "Deepika Padukone", "followers": 81000000},
    {"name": "Alia Bhatt", "followers": 87000000},
    {"name": "Narendra Modi", "followers": 93000000},
    {"name": "Akshay Kumar", "followers": 68000000},
    {"name": "Salman Khan", "followers": 71000000},
    {"name": "Shah Rukh Khan", "followers": 49000000},
    {"name": "Ranveer Singh", "followers": 48000000},
    {"name": "Katrina Kaif", "followers": 81000000},
    {"name": "Anushka Sharma", "followers": 69000000},
    {"name": "Sachin Tendulkar", "followers": 51000000},
    {"name": "MS Dhoni", "followers": 50000000},
    {"name": "Rohit Sharma", "followers": 44000000},
    {"name": "Hardik Pandya", "followers": 41000000},
    {"name": "KL Rahul", "followers": 22000000},
    {"name": "Jasprit Bumrah", "followers": 21000000},
    {"name": "Ravindra Jadeja", "followers": 24000000},
    {"name": "Shubman Gill", "followers": 18000000},
    {"name": "Suryakumar Yadav", "followers": 21000000},
    {"name": "Rishabh Pant", "followers": 15000000},
    {"name": "Yuzvendra Chahal", "followers": 10000000},
    {"name": "Ben Stokes", "followers": 3500000},
    {"name": "Joe Root", "followers": 2200000},
    {"name": "Jos Buttler", "followers": 3100000},
    {"name": "Pat Cummins", "followers": 3200000},
    {"name": "Steve Smith", "followers": 3800000},
    {"name": "David Warner", "followers": 11000000},
    {"name": "Babar Azam", "followers": 6500000},
    {"name": "Shaheen Afridi", "followers": 5000000},
    {"name": "Kane Williamson", "followers": 3000000},
    {"name": "Travis Head", "followers": 2500000},
    {"name": "Mohammed Shami", "followers": 17000000},
    {"name": "Mohammed Siraj", "followers": 14000000},
    {"name": "Sanju Samson", "followers": 18000000},
    {"name": "Ruturaj Gaikwad", "followers": 7000000},
    {"name": "Ishan Kishan", "followers": 8000000},
    {"name": "R Ashwin", "followers": 7000000},
    {"name": "Cristiano Jr", "followers": 2000000},
    {"name": "Kylian Mbappe", "followers": 124000000},
    {"name": "Erling Haaland", "followers": 39000000},
    {"name": "Vinicius Jr", "followers": 54000000},
    {"name": "Jude Bellingham", "followers": 41000000},
    {"name": "Mohamed Salah", "followers": 65000000},
    {"name": "Harry Kane", "followers": 18000000},
    {"name": "Kevin De Bruyne", "followers": 27000000},
    {"name": "Robert Lewandowski", "followers": 38000000},
    {"name": "Sergio Ramos", "followers": 65000000},
    {"name": "Luka Modric", "followers": 39000000},
    {"name": "Karim Benzema", "followers": 76000000},
    {"name": "Luis Suarez", "followers": 49000000},
    {"name": "Antoine Griezmann", "followers": 42000000},
    {"name": "Paul Pogba", "followers": 63000000},
    {"name": "Sadio Mane", "followers": 18000000},
    {"name": "Son Heung-min", "followers": 15000000},
    {"name": "Bruno Fernandes", "followers": 19000000},
    {"name": "Marcus Rashford", "followers": 18000000},
    {"name": "Jack Grealish", "followers": 12000000},
    {"name": "Lewis Hamilton", "followers": 40000000},
    {"name": "Charles Leclerc", "followers": 18000000},
    {"name": "Max Verstappen", "followers": 16000000},
    {"name": "Lando Norris", "followers": 11000000},
    {"name": "George Russell", "followers": 7000000},
    {"name": "Carlos Sainz", "followers": 12000000},
    {"name": "Fernando Alonso", "followers": 8000000},
    {"name": "Oscar Piastri", "followers": 6000000},
    {"name": "Daniel Ricciardo", "followers": 10000000},
    {"name": "Sergio Perez", "followers": 10000000},
    {"name": "Valtteri Bottas", "followers": 5000000},
    {"name": "Esteban Ocon", "followers": 3500000},
    {"name": "Pierre Gasly", "followers": 4500000},
    {"name": "Alex Albon", "followers": 4200000},
    {"name": "Yuki Tsunoda", "followers": 3200000}
]


LOGO = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗     ██╗      ██████╗ ██╗    ██╗███████╗██████╗
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗    ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝    ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗    ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║    ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_random_person():
    return random.choice(people_list)


score = 0

person_a = get_random_person()
person_b = get_random_person()

while person_a == person_b:
    person_b = get_random_person()

game_over = False

while not game_over:

    clear()

    # Uncomment if using ASCII logo
    print(LOGO)

    print(f"Current Score: {score}\n")

    print(f"A: {person_a['name']}")
    print("vs")
    print(f"B: {person_b['name']}")

    choice = input("\nWho has more Instagram followers? (A/B): ").strip().upper()

    if person_a["followers"] > person_b["followers"]:
        correct = "A"
    else:
        correct = "B"

    if choice == correct:
        score += 1
        print("\n✅ Correct!")

        # Winner stays
        person_a = person_b

        # New challenger
        person_b = get_random_person()

        while (
            person_b["name"] == person_a["name"]
        ):
            person_b = get_random_person()

        input("\nPress Enter to continue...")

    else:
        clear()
        # print(LOGO)

        print("❌ Wrong!")
        print(f"\nFinal Score: {score}\n")

        print(
            f"{person_a['name']}: {person_a['followers']:,} followers"
        )
        print(
            f"{person_b['name']}: {person_b['followers']:,} followers"
        )

        game_over = True