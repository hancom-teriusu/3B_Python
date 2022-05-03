import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
D = defaultdict(int)        # D[(a,c,g,t)] = 개수
key = [0] * 4               # key = [a, c, g, t]
idx = { 'A':0, 'C':1, 'G':2, 'T':3 }

for i in range(len(dna)):
    key[idx[dna[i]]]+=1
    if i>=K: key[idx[dna[i-K]]]-=1
    if i>=K-1: D[tuple(key)]+=1

print(max(D.values()))