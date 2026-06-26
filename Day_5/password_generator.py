import random

# Lowercase alphabets (a-z)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Numbers (0-9)
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Special characters (! to ))
symbols = [
    '!', '@', '#', '$', '%', '&', "*", '(', ')'
]

print("Welcome to python password generator!")

pwl = int(input("How many letters do you want?: "))
pwn = int(input("How many numbers do you want?: "))
pws = int(input("How many symbols do you want?: "))

pw = []

for i in range(1, pwl+1):
    l = random.choice(letters)
    pw.append(l)

for i in range(1, pwn+1):
    n = random.choice(numbers)
    pw.append(n)

for i in range(1, pws+1):
    s = random.choice(symbols)
    pw.append(s)

random.shuffle(pw)

pw = "".join(pw)

print(pw)