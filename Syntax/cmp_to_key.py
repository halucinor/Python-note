# y 좌표 오름차순, 같으면 x 값 기준 오름차순
#[(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)] -> [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

from functools import cmp_to_key

def compare(first,second):
    if first[1] > second[1]: return 1 
    elif first[1] == second[1]:
        return first[0] - second[0]
    else: return -1

xy = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

asc = sorted(xy, key=cmp_to_key(compare))
desc = sorted(xy, key=cmp_to_key(compare), reverse= True)

print(asc) # [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
print(desc) # [(0, 4), (3, 3), (2, 2), (1, 2), (1, -1)]
'''
    return 값은 첫번째 인자 first 를 기준으로 다음과 같음
    1(양수) : 크다
    -1(음수) : 작다
    0 : 같다
'''


# https://wikidocs.net/109303
# https://velog.io/@heyday_7/python-%EC%A1%B0%EA%B1%B4-%EC%A0%95%EB%A0%AC-%ED%95%98%EA%B8%B0-cmptokey

# [문제] https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3