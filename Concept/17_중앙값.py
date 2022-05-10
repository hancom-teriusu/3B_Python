from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, mid = int(input()) , int(input())
print(mid)
left, right = [], []    # max, min

for _ in range(n//2):
    for x in map(int,input().split()):
        if x<mid: heappush(left,-x)
        else: heappush(right,x)

    if len(left) < len(right):
        heappush(left, -mid)
        mid = heappop(right)

    elif len(left) > len(right):
        heappush(right, mid)
        mid = -heappop(left)

    print(mid)