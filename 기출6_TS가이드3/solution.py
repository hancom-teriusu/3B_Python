from collections import deque, defaultdict
from heapq import nlargest
from typing import List

def init(N: int, M: int, roads: List[List[int]]) -> None:
    global n, adj, cafeList, maxScore, cafeScore
    n = N
    cafeList = [[] for _ in range(n + 1)]   # cafeList[townID] = [ cafeName, ..., ]
    adj = [[] for _ in range(n + 1)]        # adj[townID] = [ townID, ..., ]
    maxScore = defaultdict(int)             # maxScore[str] = score
    cafeScore = defaultdict(int)            # cafeScore[cafeName] = score
    for i in range(M):
        adj[roads[i][0]] += [roads[i][1]]   # adj[mRoads[i][0]].append(mRoad[i][1])
        adj[roads[i][1]] += [roads[i][0]]

def addCafe(townID: int, name: str) -> None:
    cafeList[townID].append(name)
    cafeScore[name] = 0

def addScore(name: str, score: int) -> None:
    cafeScore[name] += score
    score = cafeScore[name]
    for i in range(len(name)):
        for j in range(i, len(name)):
            s = name[i:j+1]
            maxScore[s] = max(maxScore[s], score)

def getBestScore(sub: str) -> int:
    return maxScore[sub]

def getTop3Score(townID: int, step: int) -> int:
    dist = [-1] * (n + 1)
    dist[townID] = 0
    q = deque([townID])
    candi = []         # step 이내의 카페들의 가치 list
    while q:
        top = q.popleft()
        candi += [cafeScore[x] for x in cafeList[top]]
        if dist[top] == step: continue
        for x in adj[top]:
            if dist[x] == -1:
                dist[x] = dist[top] + 1
                q.append(x)

    return sum(nlargest(3, candi))