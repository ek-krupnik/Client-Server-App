from collections import Counter
import pickle

alph = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ALPH_SIZE = int(len(alph) / 2)


def upper_shift(symb, key):
    return alph[int((alph.index(symb) + key) % ALPH_SIZE)]


def lower_shift(symb, key):
    return alph[int((alph.index(symb) + key) % ALPH_SIZE + alph.index('a'))]


def train(text, model_file):

    cnt = Counter()

    for line in text:
        for symb in line:

            if alph.count(symb) > 0:
                cnt[symb] += 1

    f = open(model_file, 'wb')
    pickle.dump(cnt, f)
    f.close()

def hack(text, model_file):

    f = open(model_file, 'rb')
    benchmark_cnt = pickle.load(f)

    test_cnt = Counter()

    for line in text:
        for symb in line:

            if alph.count(symb) > 0:
                test_cnt[symb] += 1

    best_key = (0, 1e40)                                                           # key && similarity

    for key in range(0, 2 * ALPH_SIZE + 1):

        similarity = 0

        for symb in alph:
            if alph.index(symb) < 26:
                new_symb = upper_shift(symb, key)
            else:
                new_symb = lower_shift(symb, key)

            similarity += (benchmark_cnt[symb] - test_cnt[new_symb]) ** 2

        if similarity < best_key[1]:
            best_key = (key, similarity)

    return best_key[0]