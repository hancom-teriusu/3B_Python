# recommend에서 10개 구하기
from heapq import nlargest, nsmallest
from typing import List

class Cafe:
    def __init__(self, dist):
        self.myOrder = 0
        self.totOrder = 0
        self.dist = dist

def init(N: int, px: List[int], py: List[int]) -> None:
    global n, buddy, user, userXY
    n = N
    buddy = [[] for _ in range(n)]  # buddy[uid] = [uid2, uid3, .., ]
    user = [{} for _ in range(n)]   # user[uid] = { cid: Cafe() , .., }
    userXY = list(zip(px,py))

def addCafe(cid: int, x: int, y: int) -> None:
    for i in range(n):
        user[i][cid]=Cafe(abs(x-userXY[i][0])+abs(y-userXY[i][1]))

def eraseCafe(cid: int) -> None:
    for i in range(n):
        del user[i][cid]

def order(uid: int, cid: int) -> None:
    user[uid][cid].myOrder += 1
    user[uid][cid].totOrder += 1
    for x in buddy[uid]:
        user[x][cid].totOrder += 1

def beBuddy(tid: int, uid: int) -> None:
    buddy[uid].append(tid)
    buddy[tid].append(uid)
    for cid in user[uid].keys():
        user[uid][cid].totOrder += user[tid][cid].myOrder
        user[tid][cid].totOrder += user[uid][cid].myOrder

def recommend(uid: int) -> int:
    #1
    #return nlargest(10,user[uid].keys(),key=lambda cid: (user[uid][cid].totOrder, -user[uid][cid].dist, -cid))[9]

    #return nlargest(10,user[uid].items(), key = lambda d: (d[1].totOrder, -d[1].dist, -d[0]))[9][0]

    #2
    # 1) 주문 많은순   2) 거리 짧은순   3) cid 작은순
    #    a=0 ~ 3000     b=0 ~ 4,000,000   c=0 ~ 999,999
    #   ____ _______ ______
    #   (3000-a)*10^13 + b*10^6 + c
    li = [(3000 - cafe.totOrder) * int(1e+13) + cafe.dist * int(1e+6) + cid for cid, cafe in user[uid].items()]
    return nsmallest(10, li)[9] % 1000000

