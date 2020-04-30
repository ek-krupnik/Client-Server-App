import string


alph = string.ascii_uppercase + string.ascii_lowercase
ALPH_SIZE = int(len(alph) / 2)


def upper_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE]


def lower_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE + alph.index('a')]


def coding(cipher, key, text, code_type):

    result = []
    ind = 0

    if cipher == "caesar":
        key = int(key)

    for line in text:
        new_line = []

        for symb in line:

            if alph.count(symb) == 0:
                new_line += symb
                if isinstance(key, str):
                    ind = (ind + 1) % len(key)

            elif alph.index(symb) < ALPH_SIZE:                   # A <= symb <= Z
                if isinstance(key, str):                         # vigenere
                    key.upper()
                    shift = alph.index(key[ind])
                    ind = (ind + 1) % len(key)
                else:
                    shift = key

                if code_type == "decode":
                    shift = -shift

                new_line.append(upper_shift(symb, shift))

            else:
                if isinstance(key, str):
                    key.lower()
                    shift = alph.index(key[ind])
                    ind = (ind + 1) % len(key)
                else:
                    shift = key

                if code_type == "decode":
                    shift = -shift

                new_line.append(lower_shift(symb, shift))

        result.append(''.join(new_line))

    return result
