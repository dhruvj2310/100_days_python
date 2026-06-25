import random

heads = "╔════════╗\n║ HEADS  ║\n╚════════╝"

tails = "╔════════╗\n║ TAILS  ║\n╚════════╝"

if random.randint(0,1) == 0:
    print(heads)
else:
    print(tails)