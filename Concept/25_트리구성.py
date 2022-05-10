import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

child = [set() for _ in range(10001)]   # child[x] = { child id }
parent = [0] + [-1] * 10000             # parent[x] = parent id , -1 이면 없음

def isParent(cid, pid):
    while 1:
        cid = parent[cid]
        if cid==pid: return 1
        if cid==0: return 0

def getA(x):            # x와 root 노드의 거리
    dist = 0
    while x:
        dist+=1
        x = parent[x]
    return dist

def getB(x):            # x와 가장 먼 자손노드와의 거리
    dist = 0
    for y in child[x]:
        dist = max(dist, getB(y) + 1)
    return dist

def getC(x):            # x 포함 자손노드 개수
    cnt = 1
    for y in child[x]:
        cnt += getC(y)
    return cnt

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='add':
        x,y = int(cmd[1]), int(cmd[2])
        parent[x] = y
        child[y].add(x)

    elif cmd[0]=='remove':
        x = int(cmd[1])
        if x==0 or parent[x]==-1: continue
        pid = parent[x]
        child[pid].remove(x)
        child[pid] |= child[x]
        parent[x] = -1          # 지워졌음을 표시
        for cid in child[x]: parent[cid] = pid

    elif cmd[0]=='move':
        x, y = int(cmd[1]), int(cmd[2])
        if parent[x]==-1 or parent[y]==-1 or x==y: continue
        if isParent(y, x): continue

        child[parent[x]].remove(x)
        child[y].add(x)
        parent[x] = y

    else:
        x = int(cmd[1])
        print(getA(x), getB(x))
