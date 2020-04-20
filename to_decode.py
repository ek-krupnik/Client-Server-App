alph = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ALPH_SIZE = len(alph)

def caesar(text, key):
    key = int(key)
    result = []

    for line in text:
        new_line = ""

        for symb in line:
            if 'A' <= symb <= 'Z':
                new_line += alph[(alph.index(symb) - key) % ALPH_SIZE]
            elif 'a' <= symb <= 'z':
                new_line += alph[(alph.index(symb) - key - alph.index('a')) % ALPH_SIZE + alph.index('a')]
            else:
                new_line += symb

        result.append(new_line)

    return result


def vigenere(text, key):
    ind = 0
    result = []
    key = str(key)

    for line in text:
        new_line = ""

        for symb in line:

            if 'A' <= symb <= 'Z':
                key.upper()
                new_line += alph[(alph.index(symb) - alph.index(key[ind])) % ALPH_SIZE]
                ind = (ind + 1) % len(key)

            elif 'a' <= symb <= 'z':
                key.lower()
                new_line += alph[(alph.index(symb) - alph.index(key[ind]) - 2 * alph.index('a')) % ALPH_SIZE + alph.index('a')]
                ind = (ind + 1) % len(key)

            else:
                new_line += symb

        result.append(new_line)

    return result


def decoding(cipher, key, text):

    result = []

    if cipher == "caesar":
        result = caesar(text, key)
    else:
        result = vigenere(text, key)

    return result