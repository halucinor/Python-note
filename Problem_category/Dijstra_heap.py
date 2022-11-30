from heapq import heappop, heappush
import sys

'''
    heap dijstra
    O(ElogV)

    input
    6 11
    1
    1 2 2
    1 3 5 
    1 4 1
    2 3 3
    2 4 2
    3 2 3
    3 6 5
    4 3 3
    4 5 1
    5 3 1
    5 6 2
'''

input = sys.stdin.readline

INF = 10 ** 9

n , m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) # a -> b cost : c
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    heappush(q,(0, start)) # distance, node
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        # 이미 업데이트 된 경로인지 확인
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1] # i : (node, cost)

            # 현재 노드를 거쳐 다른 노드로 이동 하는 경우가 더 짧다면 distance table 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):

    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])