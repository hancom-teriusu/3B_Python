import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

prefixSet = set()
wordCnt = {}

for _ in range(int(input())):
    word = input().strip()
    prefix = ""
    ret = ""
    for ch in word:
        prefix += ch
        if prefix not in prefixSet:
            if ret=="": ret = prefix
            prefixSet.add(prefix)

    if word in wordCnt: wordCnt[word] += 1
    else: wordCnt[word] = 1

    if ret=="":         # 4번조건
        ret = word
        if wordCnt[word]>1: ret += str(wordCnt[word])

    print(ret)

