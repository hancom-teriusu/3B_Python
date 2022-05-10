import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

D = {}  # D[word] = [id, score]
idcnt = 0

for _ in range(int(input())):
    word, score = input().split()
    score = int(score)
    word = word.lower()
    if word in D:
        D[word][1] = max(D[word][1], score)
    else:
        idcnt+=1
        D[word] = [idcnt, score]
    print(*D[word])