from collections import Counter
import pickle


ALPH_SIZE = 26
alph = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def train(text, model_file):

    cnt = Counter()

    for line in text:
        for symb in line:

            if 'A' <= symb <= 'Z' or 'a' <= symb <= 'z':
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

            if 'A' <= symb <= 'Z' or 'a' <= symb <= 'z':
                test_cnt[symb] += 1

    best_key = (0, 1e40)                                                           # key && similarity

    for key in range(0, ALPH_SIZE + 1):

        similarity = 0

        for symb in alph:
            if 'A' <= symb <= 'Z':
                new_symb = chr((ord(symb) + key - ord('A')) % ALPH_SIZE + ord('A'))
            else:
                new_symb = chr((ord(symb) + key - ord('a')) % ALPH_SIZE + ord('a'))

            similarity += (benchmark_cnt[symb] - test_cnt[new_symb]) ** 2

        if similarity < best_key[1]:
            best_key = (key, similarity)

    return best_key[0]