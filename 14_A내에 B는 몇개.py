import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = [input().strip() for _ in range(n)]

### hash table 등록
def getHash(arr,x,y):
    hash = 0
    for i in range(x,x+3):      # 0~1 범위의 9개 정수 : 2진법->10진법
        for j in range(y,y+3):
            hash = hash * 2 + int(arr[x][y]=='+')
    return hash

htab = [[] for _ in range(2**9)]
#htab = defaultdict(list)
for i in range(n-3):
    for j in range(n-3):
        htab[getHash(A,i,j)].append((i,j))

### htab 검색
def isSame(x, y):
    if x > n-m or y > n-m: return 0
    for i in range(m):
        if A[x+i][y:y+m] != B[i]: return 0
    return  1

for _ in range(int(input())):
    m = int(input())
    B = [input().strip() for _ in range(m)]
    ret = 0
    hash =getHash(B,0,0)
    for x,y in htab[hash]:
        if isSame(x,y): ret+=1
    print(ret)
