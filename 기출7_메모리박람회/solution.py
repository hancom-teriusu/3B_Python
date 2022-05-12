from heapq import heappush, heappop, nlargest

class Booth:
    def __init__(self, duration, capacity):
        self.dura = duration
        self.capa = capacity
        self.finish = 0
        self.totalWait = 0
        self.wait = []         # priority 높은 순 인원 관리  wait = [[-priority, cnt], .., ]
booth = {}      # booth[bid] = Booth()

def init(boothN: int, bidArr: [int], duration: [int], capacity: [int]):
    booth.clear()
    for i in range(boothN):
        booth[bidArr[i]] = Booth(duration[i],capacity[i])

def update(tick, B):
    while B.finish<=tick and B.totalWait:
        enterCnt = min(B.totalWait, B.capa)
        B.totalWait -= enterCnt
        B.finish += B.dura
        while enterCnt:
            cnt = min(enterCnt, B.wait[0][1])
            B.wait[0][1]-= cnt
            enterCnt-=cnt
            if B.wait[0][1]==0: heappop(B.wait)

def add(tick: int, bid: int, guestNum: int, priority: int):
    B = booth[bid]
    update(tick-1, B)

    B.totalWait += guestNum
    heappush(B.wait, [-priority, guestNum])
    B.finish = max(tick, B.finish)

    update(tick, B)
    return -B.wait[0][0] if B.totalWait else 0

def search(tick: int, findCnt: int, bidArr: [int], numResult: [int]):
    li = []
    for bid, B in booth.items():        # (key, value)
        update(tick, B)
        li.append((B.totalWait, bid))

    # li = nlargest(findCnt, li)
    # for i in range(findCnt):
    #     bidArr[i] = li[i][1]
    #     numResult[i] = li[i][0]

    # nlargest(findCnt, li)= [(wait1, bid1) , (wait2, bid2), .. ]
    # *nlargest(findCnt, li) = (wait1, bid1) , (wait2, bid2), ..
    # zip(*nlargest(findCnt, li)) = (wait1, wait2, .., ) , (bid1, bid2, ..,)
    numResult[:],bidArr[:] = zip(*nlargest(findCnt, li))
