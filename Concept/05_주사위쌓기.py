import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = [0] * 7         # value copy        : immutable, numeric
b = [[]] * 7        # reference copy    : mutable

dice = [[0] * 7 for _ in range(n)]  # list comprehension

for i in range(n):
    a,b,c,d,e,f = map(int, input().split())

    # 주석 Ctrl+/
    # dice[i][a], dice[i][f] = f, a
    # dice[i][b], dice[i][d] = d, b
    # dice[i][c], dice[i][e] = e, c

    for x,y in [(a,f),(b,d),(c,e)]:
        dice[i][x], dice[i][y] = y,x

ans = 0
for bottom in range(1, 7):
    ret = 0
    for i in range(n):
        top = dice[i][bottom]

        #1. for
        # for j in range(6,0,-1):
        #     if j not in (top, bottom):
        #         ret += j
        #         break

        #2. max
        ret += max(range(1,7), key=lambda x: 0 if x in (top, bottom) else x)

        bottom = top
    ans = max(ans, ret)
print(ans)