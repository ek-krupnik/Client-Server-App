import argparse

import to_encode
import to_decode
import to_encrypt

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

def get_text():

    try:
        f = open(args.input_file, 'r')
        text = f.readlines()                                        # as list of strings
        f.close()
    except:
        text = []
        while True:
            try:
                text.append(input())
            except EOFError:
                break
    return text

def make_output(result):

    try:
        f = open(args.output_file, 'w')
        f.writelines(result)
        f.close()
    except:
        for i in result:
            print (i)

if args.code == "encode" or args.code == "decode":

    text = get_text()

    if args.code == "encode":
        result = to_encode.encoding(args.cipher, args.key, text)
    elif args.code == "decode":
        result = to_decode.decoding(args.cipher, args.key, text)

    make_output(result)

elif args.code == 'train':

    text = get_text()
    to_encrypt.train(text, args.model_file)

elif args.code == 'hack':

    text = get_text()

    key = 0
    key = to_encrypt.hack(text, args.model_file)

    result = []
    result = to_decode.decoding('caesar', key, text)
    make_output(result)