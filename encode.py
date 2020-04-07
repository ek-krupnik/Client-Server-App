
ALPH_SIZE = 26

def caesar(text, key):
    key = int(key)
    result = []

    for line in text:
        new_line = ""

        for symb in line:
            if 'A' <= symb <= 'Z':
                new_line += chr((ord(symb) + key - ord('A')) % ALPH_SIZE + ord('A'))
            elif 'a' <= symb <= 'z':
                new_line += chr((ord(symb) + key - ord('a')) % ALPH_SIZE + ord('a'))
            else:
                new_line += symb

        result.append(new_line)

    return result


def vigenere(text, key):
    ind = 0
    result = []

    for line in text:
        new_line = ""

        for symb in line:

            if 'A' <= symb <= 'Z':
                key.upper()
                new_line += chr((ord(symb) + ord(key[ind]) - 2 * ord('A')) % ALPH_SIZE + ord('A'))
                ind = (ind + 1) % len(key)

            elif 'a' <= symb <= 'z':
                key.lower()
                new_line += chr((ord(symb) + ord(key[ind]) - 2 * ord('a')) % ALPH_SIZE + ord('a'))
                ind = (ind + 1) % len(key)

            else:
                new_line += symb

        result.append(new_line)

    return result


def encoding(cipher, key, text):

    result = []

    if cipher == "caesar":
        result = caesar(text, key)
    else:
        result = vigenere(text, key)

    return result