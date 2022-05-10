import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int, input().split()))

def isValid(limit):
    curCnt, curSum = 1, 0
    for x in A:
        if curSum+x > limit:
            curCnt+=1
            curSum=x
        else:
            curSum+=x
    return curCnt<=M


s, e = max(A), sum(A)
# for i in range(s, e+1):     # linear search
#     if isValid(i):
#         print(i)
#         break

while s<=e:                   # binary search(parametric search)
    mid = (s+e)//2
    if isValid((s+e)//2): e=mid-1
    else: s=mid+1
print(s)
