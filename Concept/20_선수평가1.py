from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

maxsum, minsum, maxavg, minavg = [], [], [], []

n,m = map(int, input().split())
P = [[0,0,0] for _ in range(m+1)]       # [sum, avg, cnt]
S = [dict() for _ in range(n+1)]        # S[sid][key:pid] = value:score

def update(p, s, c):
    p[0] += s
    p[2] += c
    p[1] = round(p[0]/p[2]) if p[2] else 0

def push(pid):
    heappush(maxsum, (-P[pid][0], -pid))
    heappush(minsum, (P[pid][0], pid))
    heappush(maxavg, (-P[pid][1], -pid))
    heappush(minavg, (P[pid][1], pid))

for i in range(1, m+1):
    push(i)

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pid, score = map(int, cmd[1:])
        if pid in S[sid]: update(P[pid], score-S[sid][pid], 0)
        else: update(P[pid], score, 1)
        S[sid][pid] = score
        push(pid)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():
            update(P[pid], -score, -1)
            push(pid)
        S[sid].clear()

    elif cmd[0]=='SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while abs(pq[0][0]) != P[abs(pq[0][1])][0]: heappop(pq)
        print(abs(pq[0][1]))

    else:
        pq = maxavg if cmd[1]=='1' else minavg
        while abs(pq[0][0]) != P[abs(pq[0][1])][1]: heappop(pq)
        print(abs(pq[0][1]))