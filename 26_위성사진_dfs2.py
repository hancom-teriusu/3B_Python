import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
A = []
dx,dy = [-1,0,1,0], [0,1,0,-1]

for i in range(n):
    A.append([*input().strip()])
    #A.append(list(input().strip()))

def dfs(x,y):
    cnt = 1
    A[x][y] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if A[nx][ny] == '.': continue
        cnt += dfs(nx,ny)

    return cnt

ret = 0
for i in range(n):
    for j in range(m):
        if A[i][j]=='*':
            ret = max(ret, dfs(i,j))

print(ret)
