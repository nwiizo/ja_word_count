#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab as mc
from collections import Counter
from argparse import ArgumentParser


def parser(): 
    usage = 'Usage:python3 count_word.py [-t <FILE.txt>] [--help]'\
            .format(__file__)
    parser = ArgumentParser(usage=usage)
    parser.add_argument('-t','--text',dest='input_text',help='text file' )

    args = parser.parse_args()
    if args.input_text:
        return '{}'.format(count_csv(args.input_text))

def mecab_analysis(text):
    t = mc.Tagger("-Ochasen")
    t.parse('')
    node = t.parseToNode(text) 
    output = []
    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

def count_csv(input_text):
    text= str(open(str(input_text),"r",encoding="utf-8").read())
    words = mecab_analysis(text)
    counter = Counter(words)
    for word, count in counter.most_common():
        if len(word) > 0:
            print ("%s,%d" % (word, count))


if __name__ == '__main__':
    result = parser()
    print(result)
