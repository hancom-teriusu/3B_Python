import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
D = defaultdict(int)        # D[(a,c,g,t)] = 개수
key = [0] * 4               # key = [a, c, g, t]
idx = { 'A':0, 'C':1, 'G':2, 'T':3 }

for i in range(len(dna)-K+1):
    sub = ''.join(sorted(dna[i:i+K]))   # O(K log K)
    D[sub]+=1

print(max(D.values()))