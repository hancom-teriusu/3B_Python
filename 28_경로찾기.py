import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
A = ['']+[input().strip() for _ in range(N)]
s, e = map(int,input().split())
adj = [[] for _ in range(N+1)]      # adj[x] = [x와 인접할 수 있는 코드 번호]
prev = [-1] * (N+1)                 # prev[x] = 이전 코드 번호 , -1이면 방문 안한상태

### 그래프 구성
def isAdj(a,b):
    diff = 0
    for i in range(K):
        if a[i]!=b[i]: diff+=1
        if diff>1: return 0
    return 1

for i in range(1, N+1):
    for j in range(1, i):
        if isAdj(A[i],A[j]):
            adj[i].append(j)
            adj[j].append(i)

################

def bfs(s,e):
    q = deque([s])
    prev[s] = 0
    while q:
        x = q.popleft()
        for y in adj[x]:
            if prev[y]!=-1: continue
            q.append(y)
            prev[y] = x
            if y==e:
                path = []
                while y:
                    path.append(y)
                    y = prev[y]
                print(*path[::-1])
                return
    print(-1)

bfs(s,e)

