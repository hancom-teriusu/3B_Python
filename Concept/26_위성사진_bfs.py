import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
A = []
dx,dy = [-1,0,1,0], [0,1,0,-1]

for i in range(n):
    A.append([*input().strip()])
    #A.append(list(input().strip()))

def bfs(x,y):
    #q = deque()
    #q.append((x,y))

    q = deque([(x,y)])
    A[x][y]='.'
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if A[nx][ny]=='.': continue

            q.append((nx,ny))
            A[nx][ny]='.'
            cnt+=1

    return cnt

ret = 0
for i in range(n):
    for j in range(m):
        if A[i][j]=='*':
            ret = max(ret, bfs(i,j))

print(ret)
