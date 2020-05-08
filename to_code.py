from shifts import *


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

            else:
                if isinstance(key, str):                        # vigenere
                    if alph.index(symb) < ALPH_SIZE:            # A <= symb <= Z
                        key.lower()
                    else:
                        key.upper()
                    shift = alph.index(key[ind])
                    ind = (ind + 1) % len(key)
                else:
                    shift = key

                if code_type == "decode":
                    shift = -shift

                if alph.index(symb) < ALPH_SIZE:
                    new_line.append(lower_shift(symb, shift))
                else:
                    new_line.append(upper_shift(symb, shift))

        result.append(''.join(new_line))

    return result
