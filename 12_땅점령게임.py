import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())
D = {}
cnt = [0] * 4

for i in range(Q):
    x,y = map(int, input().split())
    pid = i % 4     # 0,1,2,3,4,5 => 0,1,2,3,0,1,2,3,..
    #key = (x,y)
    key = x*N+y     # 고유하게 정수로 나타낼수 있는 경우만 key값 대체
    if key in D:
        owner = D[key]

        if owner == pid:
           del D[key]
           cnt[pid]-=1

        elif cnt[owner] > cnt[pid]:
            D[key] = pid
            cnt[pid]+=1
            cnt[owner]-=1
    else:
        D[key] = pid
        cnt[pid]+=1

print(*cnt, sep='\n')