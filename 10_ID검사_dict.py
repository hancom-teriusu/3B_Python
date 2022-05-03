import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

D = {}  # D[id] = login(1/0)
loginCnt = 0

for _ in range(int(input())):
    cmd, id = input().split()
    if cmd=='1':
        print(int(id in D))

    elif cmd=='2':
        print(int((id in D) and D[id]))

    elif cmd=='3':
        if id not in D:
            D[id] = 0
        print(len(D))

    elif cmd=='4':
        if id in D:
            loginCnt -= D[id]
            del D[id]
        print(len(D))

    elif cmd=='5':
        if (id in D) and (D[id]==0):
            D[id] = 1
            loginCnt+=1
        print(loginCnt)

    else:
        if (id in D) and (D[id]==1):
            D[id] = 0
            loginCnt-=1
        print(loginCnt)