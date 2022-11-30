import sys

'''
    간단한 dijstra
    O(V^2)

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

dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) # a -> b cost : c
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
    return index

def dijkstra(start):
    dist[start] = 0 # 첫번째 값 초기화
    
    visited[start] = True

    #첫번째 방문 초기화
    for j in graph[start]:
        dist[j[0]] = j[1]

    for i in range(n - 1):
        # 최단 경로의 노드를 꺼내 방문 처리 -> visited set 등록
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = dist[now] + j[1]

            # 다를 노드를 거쳐 이동하는게 짧을 경우 dist 업데이트
            if cost < dist[0]:
                dist[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):

    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])

