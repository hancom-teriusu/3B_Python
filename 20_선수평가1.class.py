from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

maxsum, minsum, maxavg, minavg = [], [], [], []

n,m = map(int, input().split())

class Player:
    sum, avg, cnt = 0,0,0
    def update(self, s, c):
        self.sum += s
        self.cnt += c
        self.avg = round(self.sum/self.cnt) if self.cnt else 0

    def __lt__(self, other):
        return self.sum < other.sum

P = [Player() for _ in range(m+1)]      # P[pid] = Player()
S = [dict() for _ in range(n+1)]        # S[sid][key:pid] = value:score

class MaxData:
    def __init__(self, val, id):
        self.value = val
        self.pid = id
    def __lt__(self, other):
        return (self.value, self.pid) > (other.value, other.pid)

class MinData:
    def __init__(self, val, id):
        self.value = val
        self.pid = id
    def __lt__(self, other):
        return (self.value, self.pid) < (other.value, other.pid)

def push(pid):
    heappush(maxsum, MaxData(P[pid].sum, pid))
    heappush(minsum, MinData(P[pid].sum, pid))
    heappush(maxavg, MaxData(P[pid].avg, pid))
    heappush(minavg, MinData(P[pid].avg, pid))

for i in range(1, m+1):
    push(i)

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pid, score = map(int, cmd[1:])
        if pid in S[sid]: P[pid].update(score-S[sid][pid], 0)
        else: P[pid].update(score, 1)
        S[sid][pid] = score
        push(pid)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():
            P[pid].update(-score, -1)
            push(pid)
        S[sid].clear()

    elif cmd[0]=='SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while pq[0].value != P[pq[0].pid].sum: heappop(pq)
        print(pq[0].pid)

    else:
        pq = maxavg if cmd[1]=='1' else minavg
        while pq[0].value != P[pq[0].pid].avg: heappop(pq)
        print(pq[0].pid)