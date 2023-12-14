# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

isvisited = []


def bfs(computers, idx):
    global isvisited

    q = deque()
    q.append(idx)
    isvisited[idx] = True

    while len(q) != 0:
        node = q.pop()

        cmp_list = computers[node]

        for idx, con in enumerate(cmp_list):
            if isvisited[idx] == False and con == 1:
                q.append(idx)
                isvisited[idx] = True


def solution(n, computers):
    answer = 0

    global isvisited
    isvisited = [False] * n

    for i in range(n):
        if isvisited[i] == False:
            bfs(computers, i)
            answer += 1
    return answer