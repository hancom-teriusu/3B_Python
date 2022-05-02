import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

li = []

for _ in range(int(input())):
    cmd, val = input().split()
    if cmd=='1':
        li.append(val.lower())

    elif cmd=='2':
        if val=='0': li.sort()  #사전 오름차순
        elif val=='1': li.sort(reverse=True) #사전 내림차순
        else: li.sort(key=lambda x: (len(x), x)) # 1.길이 짧은순 2.사전 오름차순
        print(*li[:3])

    else:
        li[0] += val.lower()
        li[0] = li[0][:15]
        print(li[0])