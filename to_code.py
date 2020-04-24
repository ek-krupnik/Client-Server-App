alph = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ALPH_SIZE = int(len(alph) / 2)


def upper_shift(symb, key):
    return alph[int((alph.index(symb) + key) % ALPH_SIZE)]


def lower_shift(symb, key):
    return alph[int((alph.index(symb) + key) % ALPH_SIZE + alph.index('a'))]


def coding(cipher, key, text, code_type):

    result = []
    ind = 0

    if cipher == "caesar":
        key = int(key)

    for line in text:
        new_line = ""

        for symb in line:

            if alph.count(symb) == 0:
                new_line += symb
                if (isinstance(key, str)):
                    ind = (ind + 1) % len(key)

            elif alph.index(symb) < 26:                   # A <= symb <= Z
                if (isinstance(key, str)):              # vigenere
                    key.upper()
                    shift = alph.index(key[ind])
                    ind = (ind + 1) % len(key)
                else:
                    shift = key

                if (code_type == "decode"):
                    shift = -shift

                new_line += upper_shift(symb, shift)

            else:
                if (isinstance(key, str)):
                    key.lower()
                    shift = alph.index(key[ind])
                    ind = (ind + 1) % len(key)
                else:
                    shift = key

                if (code_type == "decode"):
                    shift = -shift

                new_line += lower_shift(symb, shift)


        result.append(new_line)

    return result