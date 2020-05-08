import pickle
import collections
from shifts import *


MAX_SIMILARITY = float('inf')


def cnt_histogram(text):

    cnt = collections.defaultdict(int)

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

    best_key = (0, MAX_SIMILARITY)                                                           # key && similarity

    for key in range(0, ALPH_SIZE):

        similarity = 0

        for symb in alph:
            if alph.index(symb) < ALPH_SIZE:
                new_symb = lower_shift(symb, key)
            else:
                new_symb = upper_shift(symb, key)

            similarity += (benchmark_cnt[symb] - test_cnt[new_symb]) ** 2

        if similarity < best_key[1]:
            best_key = (key, similarity)

    return best_key[0]
