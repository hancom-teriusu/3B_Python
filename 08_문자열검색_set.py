import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

s = set()
d = {}      # dict

for _ in range(int(input())):
    word = input().strip()
    if word in s:
        s.remove(word)
        # s -= {word}
    else:
        s.add(word)
        # s |= {word}
print(len(s))
