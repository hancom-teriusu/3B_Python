import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

prefixSet = set()
wordCnt = defaultdict(int)

#wordCnt['abc']
#print(wordCnt)

for _ in range(int(input())):
    word = input().strip()
    prefix = ""
    ret = ""
    for ch in word:
        prefix += ch
        if prefix not in prefixSet:
            if ret=="": ret = prefix
            prefixSet.add(prefix)

    wordCnt[word] += 1  # word가 등록되지 않은 경우 (word, 0) 으로 자동 등록

    if ret=="":         # 4번조건
        ret = word
        if wordCnt[word]>1: ret += str(wordCnt[word])

    print(ret)

