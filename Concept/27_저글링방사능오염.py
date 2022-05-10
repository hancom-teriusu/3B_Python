import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int,input().split())
A = [[*input().strip()] for _ in range(n)]

sy, sx = map(int,input().split())
dx,dy=[1,0,-1,0],[0,1,0,-1]

def bfs(x,y):
    q = deque([(x,y,3)])
    A[x][y] = '0'
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if A[nx][ny]=='0': continue
            q.append((nx,ny,cnt+1))
            A[nx][ny]='0'

    return cnt

print(bfs(sx-1, sy-1))

remain = 0
for i in range(n):
    remain += sum(map(int,A[i]))
print(remain)