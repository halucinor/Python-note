# https://school.programmers.co.kr/learn/courses/30/lessons/250136

import sys

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
startX, endX = sys.maxsize, -sys.maxsize
oil = 0


def solution(land):
    global startX, endX
    global oil
    size_x = len(land[0])
    size_y = len(land)

    oil_amount = [0 for _ in range(size_x)]
    is_visited = [[False for _ in range(size_x)] for _ in range(size_y)]

    def bfs(x, y):
        global startX, endX
        global oil

        que = []
        que.append((x, y))

        is_visited[y][x] = True
        oil += 1
        while que:
            x, y = que.pop(0)
            startX, endX = min(startX, x), max(endX, x)

            for dir in range(4):
                next_x = x + dx[dir]
                next_y = y + dy[dir]

                if next_x < 0 or next_x >= size_x or next_y < 0 or next_y >= size_y: continue
                if is_visited[next_y][next_x] or land[next_y][next_x] == 0: continue
                is_visited[next_y][next_x] = True
                oil += 1
                que += [(next_x, next_y)]

    for y in range(size_y):
        for x in range(size_x):
            if is_visited[y][x] or land[y][x] == 0:
                continue
            else:
                bfs(x, y)
                for col in range(startX, endX + 1):
                    oil_amount[col] += oil
                startX, endX = sys.maxsize, -sys.maxsize
                oil = 0

    answer = max(oil_amount)
    return answer


if __name__ == '__main__':
    land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
    print(solution(land))
