import argparse

import encode
import decode
import encryptor

parser = argparse.ArgumentParser(description="Encoder")
parser.add_argument('code', type=str, help="'encode' / 'decode' / 'hack' / 'train'")

parser.add_argument('--cipher', type=str, help="'caesar' or 'vigenere'")
parser.add_argument('--key', type=str, help="a number for caesar, a word for vignere")
parser.add_argument('--input-file', type=str, help="input file")
parser.add_argument('--output-file', type=str, help="output file")
parser.add_argument('--text-file', type=str, help="text file for model training")
parser.add_argument('--model-file', type=str, help="file - result of training")

args = parser.parse_args()

result = []
text = []

if args.code == "encode" or args.code == "decode":

    try:
        f = open(args.input_file, 'r')
        text = f.readlines()                                        # as list of strings
        f.close()
    except AttributeError:
        text = []
        while True:
            try:
                text.append(input())
            except EOFError:
                break

    if args.code == "encode":
        result = encode.encoding(args.cipher, args.key, text)
    elif args.code == "decode":
        result = decode.decoding(args.cipher, args.key, text)

    try:
        f = open(args.output_file, 'w')
        f.writelines(result)
        f.close()
    except AttributeError:
        for i in result:
            print (i)

elif args.code == 'train':

    try:
        f = open(args.input_file, 'r')
        text = f.readlines()                                        # as list of strings
        f.close()
    except AttributeError:
        text = []
        while True:
            try:
                text.append(input())
            except EOFError:
                break

    encryptor.train(text, args.model_file)

elif args.code == 'hack':

    try:
        f = open(args.input_file, 'r')
        text = f.readlines()                                        # as list of strings
        f.close()
    except AttributeError:
        text = []
        while True:
            try:
                text.append(input())
            except EOFError:
                break

    key = 0
    key = encryptor.hack(text, args.model_file)

    result = []
    result = decode.decoding('caesar', key, text)

    try:
        f = open(args.output_file, 'w')
        f.writelines(result)
        f.close()
    except AttributeError:
        for i in result:
            print (i)