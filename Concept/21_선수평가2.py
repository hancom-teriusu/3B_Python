from collections import defaultdict
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
        self.avg = round(self.sum*10/self.cnt) if self.cnt else 0

P = {}      # P[pid] = Player()
S = defaultdict(dict)       # S[sid] = dict({pid, score})

class MaxData:
    def __init__(self, val, name):
        self.value = val
        self.name = name
    def __lt__(self, other):
        return (self.value, self.name) > (other.value, other.name)

class MinData:
    def __init__(self, val, name):
        self.value = val
        self.name = name
    def __lt__(self, other):
        return (self.value, self.name) < (other.value, other.name)

def push(name):
    heappush(maxsum, MaxData(P[name].sum, name))
    heappush(minsum, MinData(P[name].sum, name))
    heappush(maxavg, MaxData(P[name].avg, name))
    heappush(minavg, MinData(P[name].avg, name))

names = input().split()
for i in range(m):
    P[names[i]] = Player()
    push(names[i])

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        if pname in S[sid]: P[pname].update(score-S[sid][pname], 0)
        else: P[pname].update(score, 1)
        S[sid][pname] = score
        push(pname)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pname, score in S[sid].items():
            P[pname].update(-score, -1)
            push(pname)
        S[sid].clear()

    elif cmd[0]=='SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while pq[0].value != P[pq[0].name].sum: heappop(pq)
        print(pq[0].name)

    else:
        pq = maxavg if cmd[1]=='1' else minavg
        while pq[0].value != P[pq[0].name].avg: heappop(pq)
        print(pq[0].name)