import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
dice = [1] * 7
used = [0] * 7

def recur(x):
    # base condition
    if x>n:
        print(*dice[1:n+1])
        return

    # normal condition
    st = dice[x-1] if m==2 else 1
    for i in range(st,7):
        if m==3 and used[i]: continue
        dice[x] = i
        used[i] = 1
        recur(x+1)
        used[i] = 0

recur(1)


### for loop , n=3
# for i in range(1,7):
#     st_j = i if m==2 else 1
#     for j in range(st_j,7):
#         if m==3 and i==j: continue
#
#         st_k = j if m==2 else 1
#         for k in range(st_k,7):
#             if m==3 and (i==k or j==k): continue
#             print(i,j,k)