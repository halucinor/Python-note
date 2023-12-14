# https://www.acmicpc.net/problem/1043
import sys

if __name__ == '__main__':

    read = sys.stdin.readline

    N, M = map(int, read().split())
    t, *peoples = map(int, read().split())

    truth_peoples = [False for _ in range(0, N + 1)]
    for p in peoples:
        truth_peoples[p] = True

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


    parties = []
    for _ in range(M):
        _, *party_peoples = map(int, read().split())
        parties.append(party_peoples)

        for i, num in enumerate(party_peoples):
            if i == 0: continue
            _union(party_peoples[i - 1], party_peoples[i])

    for i in range(0, N + 1):
        if truth_peoples[i]:
            truth_peoples[_find(i)] = True

    total = 0
    for party in parties:
        _type = _find(party[0])
        if not truth_peoples[_type]:
            total += 1

    print(total)
