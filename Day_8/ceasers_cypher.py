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

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(msg: str, diff: int):
    encryption = []

    for letter in msg:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = (index + diff) % len(alphabets)  # Wrap around
            encryption.append(alphabets[new_index])
        else:
            encryption.append(letter)  # Keep spaces/punctuation unchanged

    return "".join(encryption)
            

def decrypt(msg, diff):
    decryption = []

    for letter in msg:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = (index - diff) % len(alphabets)  # Wrap around
            decryption.append(alphabets[new_index])
        else:
            decryption.append(letter)  # Keep spaces/punctuation unchanged

    return "".join(decryption)



mode = input(f"{greet}\n\nType 'encrypt' or 'decrypt': ").lower().strip()
msg = str(input("Type the message to encrypt: "))
diff = int(input("shift_amt: "))

if mode == 'encrypt':
    print(encrypt(msg, diff))
elif mode == 'decrypt':
    print(decrypt(msg, diff))
else:
    print("please type a valid mode. - 'encrypt' or 'decrypt'")