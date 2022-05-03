import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
D = defaultdict(int)        # D[(a,c,g,t)] = 개수
key = [0] * 4               # key = [a, c, g, t] => a*1001^3 + c*1001^2 + g*1001 + t
idx = { 'A':0, 'C':1, 'G':2, 'T':3 }

def getKey():       # 1001진법
    hash = 0
    for k in key:
        hash = hash * 1001 + k
    return hash

for i in range(len(dna)):
    key[idx[dna[i]]]+=1
    if i>=K: key[idx[dna[i-K]]]-=1
    if i>=K-1: D[getKey()]+=1

print(max(D.values()))