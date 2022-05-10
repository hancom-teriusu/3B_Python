import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())
Q = list(map(int, input().split()))

def bisearch(x):           # x와 일치하는 인덱스
    s, e = 0, n-1
    while s<=e:
        mid = (s+e)//2
        if A[mid]==x: return mid
        elif A[mid]<x: s=mid+1
        else: e=mid-1
    return -1

def lowerBound(x):         # x이상의 첫번째 값
    s, e = 0,  n-1
    while s<=e:
        mid = (s+e)//2
        if A[mid] < x: s = mid+1
        else: e = mid-1
    return A[s]

#print('A', A)
#print('Q', Q)
for x in Q:
    print(bisearch(x), end=' ')
    #print(lowerBound(x))


