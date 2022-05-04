from collections import defaultdict
from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

D = defaultdict(int)
maxpq, minpq = [], []

for _ in range(int(input())):
    cmd, val, cnt = map(int, input().split())
    if cmd==1:
        D[val] += cnt
        print(D[val])
        heappush(maxpq, -val)
        heappush(minpq, val)

    elif cmd==2:
        D[val] -= cnt
        print(max(0,D[val]))
        if D[val]<=0: del D[val]

    elif cmd==3:

        pq = maxpq if val else minpq    # reference copy
        ret = 0
        while cnt and pq:
            worth = abs(pq[0])
            if worth not in D:
                heappop(pq)
                continue

            sellCnt = min(cnt, D[worth])
            cnt-=sellCnt
            D[worth]-=sellCnt

            if D[worth]==0:
                heappop(pq)
                del D[worth]

            ret += worth * sellCnt

        print(ret)