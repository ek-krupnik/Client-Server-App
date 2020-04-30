import argparse

import to_code
import to_encrypt

parser = argparse.ArgumentParser(description="Encoder")
subparsers = parser.add_subparsers(dest="code")

parser_encode = subparsers.add_parser('encode', help="Choose a mode")
parser_encode.add_argument('--cipher', type=str, help="'caesar' or 'vigenere'")
parser_encode.add_argument('--key', type=str, help="a number for caesar, a word for vignere")
parser_encode.add_argument('--input-file', type=str, help="input file")
parser_encode.add_argument('--output-file', type=str, help="output file")

parser_decode = subparsers.add_parser('decode', help="Choose a mode")
parser_decode.add_argument('--cipher', type=str, help="'caesar' or 'vigenere'")
parser_decode.add_argument('--key', type=str, help="a number for caesar, a word for vignere")
parser_decode.add_argument('--input-file', type=str, help="input file")
parser_decode.add_argument('--output-file', type=str, help="output file")

parser_train = subparsers.add_parser('train', help="Choose a mode")
parser_train.add_argument('--text-file', type=str, help="text file for model training")
parser_train.add_argument('--model-file', type=str, help="file - result of training")

parser_hack = subparsers.add_parser('hack', help="Choose a mode")
parser_hack.add_argument('--input-file', type=str, help="input file")
parser_hack.add_argument('--output-file', type=str, help="output file")
parser_hack.add_argument('--model-file', type=str, help="file - result of training")


args = parser.parse_args()

result = []
text = []


def get_text(input_file):

    try:
        f = open(input_file, 'r')
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

    text = get_text(args.input_file)
    result = to_code.coding(args.cipher, args.key, text, args.code)

    make_output(result)

elif args.code == 'train':

    text = get_text(args.text_file)
    to_encrypt.train(text, args.model_file)

elif args.code == 'hack':

    text = get_text(args.input_file)

    key = 0
    key = to_encrypt.hack(text, args.model_file)

    result = []
    result = to_code.coding('caesar', key, text, 'decode')
    make_output(result)
