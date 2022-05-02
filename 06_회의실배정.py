import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
#li = [list(map(int,input().split())) for _ in range(n)]
#li.sort(key=lambda x: x[2])

# O(n log n)
li = sorted([tuple(map(int,input().split())) for _ in range(n)], key = lambda x:x[2])

end = 0
select = []
for id, s, e in li:
    if end<=s:
        end = e
        select.append(id)

print(len(select))
print(*select)