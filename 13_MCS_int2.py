import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
D = defaultdict(int)
key = 0
base = {'A':1001**3, 'C':1001**2, 'G':1001, 'T':1}

for i in range(len(dna)):
    key+=base[dna[i]]
    if i>=K: key-=base[dna[i-K]]
    if i>=K-1: D[key]+=1

print(max(D.values()))