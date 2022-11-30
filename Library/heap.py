# https://security-nanglam.tistory.com/433
from heapq import heappush, heappop

# heapq는 element 첫번째 요소를 기준으로 자료를 넣고 빼는 작업을 수행

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heappush(h, value)
    
    for _ in range(len(h)):
        result.append(heappop(h))

    return result

def desc_heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heappush(h, -1 * value)

    for _ in range(len(h)):
        result.append(-1 * heappop(h))
    
    return result

result = heapsort([1,2,3,9,7,7,1,2,69,3,7,5,8,9])
print(result) #[1, 1, 2, 2, 3, 3, 5, 7, 7, 7, 8, 9, 9, 69]

result = desc_heapsort([1,2,3,9,7,7,1,2,69,3,7,5,8,9])
print(result) #[69, 9, 9, 8, 7, 7, 7, 5, 3, 3, 2, 2, 1, 1]