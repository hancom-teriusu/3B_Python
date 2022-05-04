from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

maxpq, minpq, abspq = [], [], []

for _ in range(int(input())):
    x = int(input())
    if x==0:
        if not maxpq: print(-1)
        else:
            print(-heappop(maxpq), heappop(minpq), heappop(abspq)[1])

    else:
        heappush(maxpq, -x)
        heappush(minpq, x)
        heappush(abspq, (abs(x), x))    # 1.절대값 작은순 2. x 작은순