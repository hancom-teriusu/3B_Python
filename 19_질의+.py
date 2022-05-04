from heapq import heappush, heapify, heappop
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

S = [0] * 100001
minpq, maxpq = [], []

def get(pq):
    valid = []
    while len(valid) < 3 and pq:
        score, id = heappop(pq)
        if S[abs(id)] != abs(score): continue          # 최신정보확인
        if valid and valid[-1][1] == id: continue      # 중복확인
        valid.append((score, id))

    if len(valid) < 3: print(-1)
    else: print(abs(valid[-1][1]))

    for x in valid: heappush(pq,x)


for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0]==1:
        id, score = cmd[1:]
        S[id] = score
        heappush(minpq, (score, id))
        heappush(maxpq, (-score, -id))

    elif cmd[0]==2:
        id = cmd[1]
        S[id] = 0

    elif cmd[0]==3:
        # 1. 일괄처리
        get(minpq)

        # 2. 따로처리
        # valid = []
        # while len(valid) < 3 and minpq:
        #     score, id = heappop(minpq)
        #     if S[id] != score: continue                    # 최신정보확인
        #     if valid and valid[-1][1] == id: continue      # 중복확인
        #     valid.append((score, id))
        #
        # if len(valid) < 3: print(-1)
        # else: print(valid[-1][1])
        #
        # for x in valid: heappush(minpq,x)

    else:
        # 1
        get(maxpq)

        # 2
        # valid = []
        # while len(valid) < 3 and maxpq:
        #     score, id = heappop(maxpq)
        #     if S[-id] != -score: continue                  # 최신정보확인
        #     if valid and valid[-1][1] == id: continue      # 중복확인
        #     valid.append((score, id))
        # if len(valid) < 3: print(-1)
        # else: print(-valid[-1][1])
        # for x in valid: heappush(maxpq,x)
