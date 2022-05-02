import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dq = deque()

def insert_(pos, value):
    if pos==1:
        dq.append(value)
    else:
        dq.appendleft(value)

def erase_(pos, value):
    cnt = 0
    if pos == 0:
        i = 0
        while i < len(dq):
            if dq[i] >= value:
                del dq[i]
                cnt+=1
                if cnt>=3: break
            else: i+=1

    else:
        i = len(dq) - 1
        while i>=0 and cnt<3:
            if dq[i]>=value:
                del dq[i]
                cnt+=1
            i-=1

def sort_(value):
    #dq.sort()               # dq 자체를 정렬
    #sorted(dq)              # dq를 정렬한 dqst 반환, 원본 그대로

    global dq
    dq = deque(sorted(dq, key=lambda x : (abs(value-x), x)))

def print_(pos):
    if pos==0:
        print(*dq)  # unpacking
    else:
        print(*reversed(dq))


q = int(input())
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0]==1: insert_(*cmd[1:])
    elif cmd[0]==2: erase_(cmd[1],cmd[2])
    elif cmd[0]==3: sort_(cmd[1])
    else: print_(cmd[1])