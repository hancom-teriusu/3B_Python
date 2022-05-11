# 와일드카드 문자 사용
from collections import defaultdict

orgDict = set()
diffDict = defaultdict(list)

def init(N: int, str: list) -> None:
    global S
    S = ''.join(str)
    orgDict.clear()
    diffDict.clear()

def addDict(word: list) -> None:
    W = ''.join(word)
    orgDict.add(W)
    for i in range(len(W)):
        diffDict[W[:i]+'_'+W[i+1:]].append(W)

def removeDict(word: list) -> None:
    W = ''.join(word)
    orgDict.remove(W)
    for i in range(len(W)):
        diffDict[W[:i]+'_'+W[i+1:]].remove(W)

def correctWord(start: int, end: int) -> int:
    global S
    newWord = []
    cnt = 0
    for word in S[start:end+1].split('_'):
        select = chr(ord('z')+1)
        if word not in orgDict:
            for i in range(len(word)):      #word = abcd => _bcd, a_cd, ab_d, abc_
                li = diffDict[word[:i]+'_'+word[i+1:]]
                if li: select = min(li + [select])
        if select == chr(ord('z')+1): select = word
        else: cnt+=1
        newWord.append(select)
    S = S[:start] + '_'.join(newWord) + S[end+1:]
    return cnt

def destroy(result: list) -> None:
    result[:] = list(S)