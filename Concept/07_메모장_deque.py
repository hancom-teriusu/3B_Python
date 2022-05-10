import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m,q = map(int, input().split())
dq = [deque() for _ in range(n)]
cur, cnt = 0, 0

for ch in input().strip():
    dq[cnt//m].append(ch)
    cnt+=1

for _ in range(q):
    cmd = input().split()

    if cmd[0]=='insert':
        x, y = cur//m , cur%m
        dq[x].insert(y, cmd[1])
        while len(dq[x]) > m:
            dq[x+1].appendleft(dq[x].pop())
            x+=1
        cur+=1
        cnt+=1

    elif cmd[0]=='erase':
        if cur==0: continue
        cur-=1
        cnt-=1
        x,y= cur//m, cur%m
        del dq[x][y]
        while dq[x+1]:
            dq[x].append(dq[x+1].popleft())
            x+=1

    else:
        x,y= int(cmd[1]), int(cmd[2])
        cur = min(cnt, x*m+y)
        if cur<cnt: print(dq[x][y])
        else: print('*')