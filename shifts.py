import string


alph = string.ascii_letters
ALPH_SIZE = int(len(alph) / 2)


def lower_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE]


def upper_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE + alph.index('A')]
