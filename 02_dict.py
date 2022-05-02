import sys
from heapq import nlargest

sys.stdin = open('input.txt')
input = sys.stdin.readline

#D = dict()
D = {}          # D[key] = value , D[pid] = [salary, C, J, P]

# d = {'d':3,  'b':2, 'c':1}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(min(d, key=lambda x : d[x]))
# print(min(d.values()))

for _ in range(int(input())):
    cmd = input().split()
    data = list(map(int, cmd[1:]))

    if cmd[0]=='register':
        D[data[0]] = data[1:]
        # data[0] = pid , data[1:] = [salary, C, J, P]

    elif cmd[0]=='cancel':
        if data[0] in D:
            del D[data[0]]

    elif cmd[0]=='update':
        pid, flag, X = data
        if pid in D:
            D[pid][flag+1] = X

    elif cmd[0] == 'hire_min':
        # 1. salary 작은순
        # 2. pid 작은순
        pid = min(D.items(), key = lambda x: (x[1][0], x[0]))[0]     # x[0]=pid, x[1]=[salary, C, J, P]
        print(pid)
        del D[pid]

    else:
        # 1. 평균역량 높은순   : (C+J+P)/3 -> 합으로 처리 (C+J+P)
        # 2. pid 큰순

        ## 1. max : O(n * 3)
        # for _ in range(3):
        #     pid = max(D, key = lambda x: (sum(D[x][1:]), x))
        #     print(pid, end=' ')
        #     del D[pid]
        # print()

        ## 2. nlargest : O(n + 3 log n) or O(n log 3)
        best = nlargest(3, D.items(), key = lambda x : (sum(x[1][1:]), x))
        for pid, _ in best:
            print(pid, end = ' ')
            del D[pid]
        print()