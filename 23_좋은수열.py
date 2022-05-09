import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
A = [0] * n

def isBad(m):
    i=1
    while m-i*2>=0:
        if A[m-i*2:m-i] == A[m-i:m]: return 1
        i+=1
    return 0

def recur(x):
    if x>=n:
        print(*A, sep='')
        return 1

    for i in range(1,4):
        A[x] = i
        if isBad(x+1): continue
        if recur(x+1): return 1

    return 0

recur(0)