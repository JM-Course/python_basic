#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1. apple_wiki.txt의 텍스트 데이터를 읽기
2. 공백을 기준으로 tokenize하기 (lower, ".", "," 문자 제거)
3. indexing하기 (word2id, id2word)
3. word2id, id2word pickle로 저장하기
"""

import re
from collections import Counter
import pickle


def main():
    vocab = Counter()
    with open("./apple_wiki.txt", "r") as f:
        # 텍스트 읽기, read() 사용
        data = f.read()
        # lower
        data = data.lower()
        # . , 제거 (re 사용)
        data = re.sub("[,.]", "", data)
        # 공백 기준 tokenize
        tokens = data.split()
        # vocab에 토큰 update
        vocab.update(tokens)

    word2id = dict()
    for word in vocab:
        # indexing
        word2id[word] = len(word2id)
    # id2word 만들기
    id2word = dict(zip(word2id.values(), word2id.keys()))

    with open("./indexing.bin", "wb") as f:
        # [word2id, id2word] 리스트 형태로 저장, pickle dump 사용
        pickle.dump([word2id, id2word], f)


if __name__ == "__main__":
    main()

    with open("./indexing.bin", "rb") as f:
        word2id, id2word = pickle.load(f)
        print(word2id)
        print(id2word)
