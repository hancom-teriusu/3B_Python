def init(N):
    global emptyS , emptyE, used, n
    emptyS = {}   # emptyS[start] = size
    emptyE = {}   # emptyE[end] = start
    used = {}     # used[start] = end
    emptyS[0] = N
    emptyE[N] = 0
    n = N

def allocate(size):
    # emptyS.items() : [(start, size) ,... ]
    emptyStart, emptySize = min(emptyS.items(), key=lambda x: (x[1], x[0]) if x[1]>=size else (n+1,0))  # O(n)
    if emptySize < size: return -1

    used[emptyStart] = emptyStart + size

    remainStart = emptyStart + size
    remainEnd = emptyStart + emptySize
    remainSize = emptySize - size

    del emptyS[emptyStart]      # 기존 빈공간 제거
    del emptyE[remainEnd]

    if remainSize:
        emptyS[remainStart] = remainSize
        emptyE[remainEnd] = remainStart

    return emptyStart

def deallocate(start):
    if start not in used: return -1

    end = used[start]
    size = end - start
    del used[start]

    if start in emptyE:
        newStart = emptyE[start]
        del emptyE[start]
        start = newStart

    if end in emptyS:
        newEnd = end + emptyS[end]
        del emptyS[end]
        end = newEnd

    emptyS[start] = end-start
    emptyE[end] = start

    return size