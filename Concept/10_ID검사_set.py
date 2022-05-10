import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

member, login = set(), set()

for _ in range(int(input())):
    cmd, id = input().split()
    if cmd=='1':
        print(int(id in member))

    elif cmd=='2':
        print(int(id in login))

    elif cmd=='3':
        member.add(id)
        #member |= {id}
        print(len(member))

    elif cmd=='4':
        #if id in member: member.remove(id)
        #if id in login: login.remove(id)

        member -= {id}
        login -= {id}

        print(len(member))

    elif cmd=='5':
        if id in member: login.add(id)
        print(len(login))

    else:
        login-={id}
        print(len(login))