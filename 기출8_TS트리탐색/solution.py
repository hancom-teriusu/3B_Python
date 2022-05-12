from heapq import heappush, heappop
from typing import List

def dfs(x):
	if visited[x]==vcnt: return
	visited[x] = vcnt
	table[src][x] = dest
	for y in adj[x]: dfs(y)

def init(N: int, parent: List[int]) -> None:
	global adj, curTick, curCity, pq, caseCity, table, src, dest, visited, vcnt
	curTick, curCity = 0, 0
	adj = [[] for _ in range(N)]
	pq = []									# (-priority, tick, caseID)
	caseCity = []							# caseCity[caseID] = cityID	, 취소 되면 -1
	table = [[0] * N for _ in range(N)]		# table[curCity][destCity] = nextCity

	for i in range(1,N):					# 그래프 구성
		adj[i].append(parent[i])
		adj[parent[i]].append(i)

	vcnt = 0
	visited = [0] * N
	for src in range(N):					# table[src][x] = dest 구성
		vcnt+=1
		visited[src] = vcnt
		for dest in adj[src]: dfs(dest)

def update(tick):
	global curTick, curCity
	while curTick < tick:
		curTick+=1
		while pq and caseCity[pq[0][2]]==-1:
			heappop(pq)
		if not pq:
			break

		destCity = caseCity[pq[0][2]]
		if destCity == curCity: heappop(pq)
		else: curCity = table[curCity][destCity]

	curTick = tick

def occur(timeStamp: int, caseID: int, townNum: int, prior: int) -> None:
	update(timeStamp)
	caseCity.append(townNum)
	heappush(pq, (-prior, timeStamp, caseID))

def cancel(timeStamp: int, caseID: int) -> None:
	update(timeStamp)
	caseCity[caseID] = -1

def position(timeStamp: int) -> int:
	update(timeStamp)
	return curCity