greet = """
   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
  ██║     ███████║█████╗  ███████╗███████║██████╔╝
  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

             ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
            ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
            ██║     ██║██████╔╝███████║█████╗  ██████╔╝
            ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
            ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
             ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def encrypt(msg: str, diff: int):
    encrypted_msg = ""

    for letter in msg:
        if letter in lowercase:
            shift = lowercase.index(letter) + diff
            shift %= len(lowercase)
            encrypted_msg += lowercase[shift]

        elif letter in uppercase:
            shift = uppercase.index(letter) + diff
            shift %= len(uppercase)
            encrypted_msg += uppercase[shift]

        else:
            encrypted_msg += letter

def decrypt(msg: str, diff: int):
    encrypted_msg = ""

    for letter in msg:
        if letter in lowercase:
            shift = lowercase.index(letter) - diff
            shift %= len(lowercase)
            encrypted_msg += lowercase[shift]

        elif letter in uppercase:
            shift = uppercase.index(letter) - diff
            shift %= len(uppercase)
            encrypted_msg += uppercase[shift]

        else:
            encrypted_msg += letter


mode = input(f"{greet}\n\nType 'encrypt' or 'decrypt': ").lower().strip()
msg = str(input("Type the message to encrypt: "))
diff = int(input("shift_amt: "))

if mode == 'encrypt':
    print(encrypt(msg, diff))
elif mode == 'decrypt':
    print(decrypt(msg, diff))
else:
    print("please type a valid mode. - 'encrypt' or 'decrypt'")