import sys
import time

#from solution_heapq_int import init, addCafe, eraseCafe, order, beBuddy, recommend
#from solution_heapq_tuple import init, addCafe, eraseCafe, order, beBuddy, recommend
from solution_nsmallest import init, addCafe, eraseCafe, order, beBuddy, recommend

CMD_INIT = 100
CMD_ADD_RESTAURANT = 200
CMD_REMOVE_RESTAURANT = 300
CMD_ORDER = 400
CMD_BE_FRIEND = 500
CMD_RECOMMEND = 600

def pp(*args):
    if testcase==2: print(*args)

def run():
    query = int(input())
    ok = False
    n = 0
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            n = int(next(input_iter))
            list_px = list(map(int, input().split()))
            list_py = list(map(int, input().split()))
            init(n, list_px, list_py)
            ok = True
        elif cmd == CMD_ADD_RESTAURANT:
            pp(i, 'ADD')
            cid = int(next(input_iter))
            x = int(next(input_iter))
            y = int(next(input_iter))
            addCafe(cid, x, y)
        elif cmd == CMD_REMOVE_RESTAURANT:
            pp(i, 'REMOVE')
            cid = int(next(input_iter))
            eraseCafe(cid)
        elif cmd == CMD_ORDER:
            pp(i, 'ORDER')
            uid = int(next(input_iter))
            cid = int(next(input_iter))
            order(uid, cid)
        elif cmd == CMD_BE_FRIEND:
            pp(i, 'BUDDY')
            tid = int(next(input_iter))
            uid = int(next(input_iter))
            beBuddy(tid, uid)
        elif cmd == CMD_RECOMMEND:
            uid = int(next(input_iter))
            pp(i, 'RECOMMEND')
            ret = recommend(uid)
            ans = int(next(input_iter))
            if ans != ret:
                if testcase==2: print(i, uid, ret, ans)
                ok = False
    return ok


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    start = time.time()
    global testcase
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
    print(time.time() - start)

