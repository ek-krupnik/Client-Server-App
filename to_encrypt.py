import pickle
import string


alph = string.ascii_uppercase + string.ascii_lowercase
ALPH_SIZE = int(len(alph) / 2)
MAX_SIMILARITY = 1e40


def upper_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE]


def lower_shift(symb, key):
    return alph[(alph.index(symb) + key) % ALPH_SIZE + alph.index('a')]


def cnt_histogram(text):

    cnt = {symb : 0 for symb in alph}

    for line in text:
        for symb in line:

            if alph.count(symb) > 0:
                cnt[symb] += 1

    return cnt


def train(text, model_file):

    cnt = cnt_histogram(text)

    f = open(model_file, 'wb')
    pickle.dump(cnt, f)
    f.close()


def hack(text, model_file):

    f = open(model_file, 'rb')
    benchmark_cnt = pickle.load(f)

    test_cnt = cnt_histogram(text)

    print (benchmark_cnt)
    print()
    print (test_cnt)

    best_key = (0, MAX_SIMILARITY)                                                           # key && similarity

    for key in range(0, 2 * ALPH_SIZE + 1):

        similarity = 0

        for symb in alph:
            if alph.index(symb) < ALPH_SIZE:
                new_symb = upper_shift(symb, key)
            else:
                new_symb = lower_shift(symb, key)

            similarity += (benchmark_cnt[symb] - test_cnt[new_symb]) ** 2

        if similarity < best_key[1]:
            best_key = (key, similarity)

    print (best_key)
    return best_key[0]
