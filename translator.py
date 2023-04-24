# Morse Code Translator Using Python. 

MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..'}


# Defining a function to encrypt the string from the dict

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks at the dict and adds corresponding code and separates with a space (' ') for different chars
            cipher += MORSE_DICT[
                          letter] + ' '
        else:
            cipher += ' '  # 1 space = different letter; 2 spaces = different word

    return cipher


# Defining a function decrypt the string from the code to English

def decrypt(message):
    message += ' '  # Adding an extra space at the end to access the last bit of code
    decipher = ''
    citext = ''
    for letter in message:

        if letter != ' ':  # Checking for space here - note how a missing space earlier ruined the whole code!
            # Created a counter to keep track of spaces (initialising a counter before the for loop) -
            # needed to be in the 'if' loop and not outside
            i = 0
            citext += letter  # Stores code of a single character

        else:

            i += 1  # If i = 1, that indicates a new char

            if i == 2:
                decipher += ' '  # Adding space to indicate new words

            else:
                decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                citext = ''

    return decipher


def main():
    message = input("Enter what you seek to encrypt: ").upper()
    result = encrypt(message.upper())
    print(result)

    message = input("Enter what you wish to decrypt: ")
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
