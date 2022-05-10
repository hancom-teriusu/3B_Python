import sys
from solution import init, pushBack, popBack, reverseStr, getCount

CMD_INIT = 1
CMD_APPEND = 2
CMD_popBack = 3
CMD_reverseStr = 4
CMD_COUNT = 5

def pp(*args):
    if tc==0: print(*args)

def ppp(*args):
    if tc == 25: print(*args)

def run():
    query_cnt = int(sys.stdin.readline())
    correct = False

    for q in range(query_cnt):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            mStr = next(inputs)
            init(mStr)
            pp(q, 'INIT', mStr)
            correct = True

        elif cmd == CMD_APPEND:
            mWord = next(inputs)
            pp(q, 'PUSH', mWord)
            if correct:
                pushBack(mWord)

        elif cmd == CMD_popBack:
            k = int(next(inputs))

            pp(q, 'POP', k)
            if correct:
                popBack(k)

        elif cmd == CMD_reverseStr:
            pp(q, 'REVERSE')
            if correct:
                reverseStr()

        elif cmd == CMD_COUNT:
            mWord = next(inputs)
            pp(q, 'COUNT', mWord)
            ret = -1
            if correct:
                ret = getCount(mWord)

            ans = int(next(inputs))
            pp('ret=',ret, 'ans=',ans)
            if ret != ans:
                if ret!=-1: ppp(q, 'COUNT', mWord)
                if ret!=-1: ppp('ret=',ret, 'ans=',ans)
                correct = False

    return correct


def main():
    sys.stdin = open('input.txt', 'r')
    TC, MARK = map(int, sys.stdin.readline().split())

    global tc
    for tc in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)


if __name__ == '__main__':
    main()