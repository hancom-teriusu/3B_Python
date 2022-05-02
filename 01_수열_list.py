import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

li = []
li2 = list()
li3 = [x for x in range(1,11)]

def insert_(pos, value):
    global li
    if pos==1:
        li.append(value)
        #li = [value]
    else: li.insert(0, value)

def erase_(pos, value):
    cnt = 0
    if pos == 0:
        i = 0
        while i < len(li):
            if li[i] >= value:
                del li[i]
                cnt+=1
                if cnt>=3: break
            else: i+=1

    else:
        i = len(li) - 1
        while i>=0 and cnt<3:
            if li[i]>=value:
                del li[i]
                cnt+=1
            i-=1

def comp(x):
    return (abs(V-x), x)

def sort_(value):
    global V
    V=value

    li.sort()               # <
    li.sort(reverse=True)   # >
    li.sort(key=abs)        # 절대값 오름차순

    li.sort(key=comp)
    li.sort(key=lambda x : (abs(value-x), x))

def print_(pos):
    if pos==0:
        #for x in li: print(x, end=' ')
        #print()
        print(*li)  # unpacking

    else:
        print(*li[::-1])


q = int(input())
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0]==1: insert_(*cmd[1:])
    elif cmd[0]==2: erase_(cmd[1],cmd[2])
    elif cmd[0]==3: sort_(cmd[1])
    else: print_(cmd[1])