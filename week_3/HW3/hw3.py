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
        # 텍스트 읽기 (read() 사용)

        # lower

        # . , 제거 (re 사용)

        # 공백 기준 tokenize

        # vocab에 토큰 update

        pass

    word2id = dict()
    for word in vocab:
        # indexing
        pass
    # id2word 만들기


    with open("./indexing.bin", "wb"):
        # [word2id, id2word] 리스트 형태로 저장, pickle dump 사용
        pass


if __name__ == "__main__":
    main()
