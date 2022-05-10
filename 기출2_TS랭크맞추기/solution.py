def find(x, query):
    s, e = 0, len(remainId)         # 구간: s 포함, e 미포함
    while e-s>5:
        m = max(s+5, (s+e)//2)
        if query(m-s, remainId[s:m], 0)==x: e=m
        else: s=m
    for i in range(s,e):
        if query(len(remainId)-1, remainId[:i]+remainId[i+1:], 0)!=x: return remainId[i]

def getRank(retRank: [int], query) -> None:
    global remainId
    remainId = list(range(1000))        # [0,1,2,3,..,998,999]
    minId = []
    for i in range(4):
        minId.append(find(i, query))    # rank가 i(0,1,2,3)인 id 반환, minId 추가
        retRank[minId[i]] = i
        remainId.remove(minId[i])
    for x in remainId:
        retRank[x] = query(5, minId+[x], 1)