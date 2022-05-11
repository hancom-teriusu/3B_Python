# 교정 가능한 모든 단어 등록
from collections import defaultdict

orgDict = set()                 # orgDict = { 사전의 단어,.. }
diffDict = defaultdict(list)    # diffDict[교정가능단어] = [사전의 단어,..]
char = list(map(chr, range(ord('a'), ord('z')+1)))  # ord('a') = 97    chr(97) = 'a'    # char = [ 'a' , 'b' , ... , 'z' ]

def init(N: int, str: list) -> None:
    global S
    S = ''.join(str)
    orgDict.clear()
    diffDict.clear()

def addDict(word: list) -> None:
    W = ''.join(word)
    orgDict.add(W)
    for i in range(len(W)):
        for c in char:
            diffDict[W[:i]+c+W[i+1:]].append(W)

def removeDict(word: list) -> None:
    W = ''.join(word)
    orgDict.remove(W)
    for i in range(len(W)):
        for c in char:
            diffDict[W[:i]+c+W[i+1:]].remove(W)

def correctWord(start: int, end: int) -> int:
    global S
    newWord = []
    cnt = 0
    for word in S[start:end+1].split('_'):  #['abb', 'def', 'ghj'] 'abb_def_ghj'
        if word not in orgDict and diffDict[word]:
            newWord.append(min(diffDict[word]))
            cnt+=1
        else:
            newWord.append(word)
    S = S[:start] + '_'.join(newWord) + S[end+1:]
    return cnt

def destroy(result: list) -> None:
    result[:] = list(S)     # value copy
