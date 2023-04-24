import sys

# Morse Code Translator Using Python.

MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..'}


# Defining a function to encrypt the string from the dict

def encrypt(message):
    cipher = []
    for letter in message:
        if letter != ' ':

            # Looks at the dict and adds corresponding code and separates with a space (' ') for different chars
            cipher.append(MORSE_DICT[letter])
        else:
            cipher.append('/')  # 1 space = different letter; 2 spaces = different word

    return ' '.join(cipher)


# Defining a function decrypt the string from the code to English

def decrypt(message):
    decipher = []
    for word in message.strip().split("/"):
        constructed_word = []
        for letter in word.strip().split(" "):
            inv = dict([(MORSE_DICT[l], l) for l in MORSE_DICT])

            constructed_word.append(inv.get(letter, ''))
        decipher.append(''.join(constructed_word))

    return ' '.join(decipher).lower()


def main(args):
    if len(args) < 2:
        print("Please enter a command!")
        return

    if args[1] == 'encrypt':
        if len(args) == 3:
            path = args[2]
            with open(path, 'r') as f:
                message = f.read()
        else:
            message = input("Enter what you seek to encrypt: ").upper()

        result = encrypt(message.upper())
        print(result)
    elif args[1] == 'decrypt':
        if len(args) == 3:
            path = args[2]
            with open(path, 'r') as f:
                message = f.read()
        else:
            message = input("Enter what you wish to decrypt: ").upper()

        result = decrypt(message)
        print(result)


if __name__ == '__main__':
    main(sys.argv)
