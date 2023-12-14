# 서로 독립적인 집합을 찾는 알고리즘
N = 10
parents = [i for i in range(0, N + 1)]


def _find(x):
    global parents
    if parents[x] == x:
        return parents[x]
    else:
        return _find(parents[x])


def _union(a, b):
    global parents
    a = _find(a)
    b = _find(b)

    if a != b:
        if a > b:
            parents[a] = b
        else:
            parents[b] = a
