from collections import deque, defaultdict

dq = deque()
cnt = defaultdict(int)

def init(mStr: str):
    global dq, cnt, rev
    dq.clear()
    cnt.clear()
    rev = False

    for c in mStr:
        dq.append(c)
        update(1)

def update(one):           # rev = 1/0 통합 업데이트
    if rev: r = range(0, min(4, len(dq)))
    else: r = range(len(dq)-1, max(len(dq)-5, -1), -1)
    sub = ''
    for i in r:
        if rev: sub += dq[i]
        else: sub = dq[i] + sub
        cnt[sub]+=one

def left(one):              # rev = 1 일때 업데이트
    sub = ''
    for i in range(range(0, min(4, len(dq)))):
        sub += dq[i]
        sub[sub]+=one

def right(one):             # rev = 0 일때 업데이트
    sub = ''
    for i in range(len(dq)-1, max(len(dq)-5, -1), -1):
        sub = dq[i] + sub
        sub[sub]+=one

def pushBack(mWord: str):
    global dq
    for c in mWord:
        if rev: dq.appendleft(c)
        else: dq.append(c)
        update(1)

def popBack(k: int):
    for i in range(k):
        update(-1)
        if rev: dq.popleft()
        else: dq.pop()

def reverseStr():
    global rev
    rev = not rev

def getCount(mWord: str) -> int:
    if rev: mWord = mWord[::-1]
    return cnt[mWord]