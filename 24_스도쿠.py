import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

A = [list(map(int, input().split())) for _ in range(9)]
zero = []
row = [[0] * 10 for _ in range(9)]  # row[x][i]
col = [[0] * 10 for _ in range(9)]  # col[y][i]
sub = [[0] * 10 for _ in range(9)]  # sub[(x/3)*3+(y/3)][i]

for i in range(9):
    for j in range(9):
        if A[i][j]==0: zero.append((i,j))
        else:
            row[i][A[i][j]]=1
            col[j][A[i][j]]=1
            sub[i//3*3+j//3][A[i][j]]=1

def recur(c):
    if c>=len(zero):
        for i in range(9):
            print(*A[i])
        return 1

    x, y = zero[c]
    z = x//3*3+y//3
    for i in range(1,10):
        if row[x][i] or col[y][i] or sub[z][i]: continue
        A[x][y] = i
        row[x][i], col[y][i], sub[z][i] = 1, 1, 1
        if recur(c+1): return 1
        row[x][i], col[y][i], sub[z][i] = 0, 0, 0

    return 0

recur(0)