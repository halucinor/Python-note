#파이썬에서 큐(queue) 자료 구조 사용하기 https://www.daleseo.com/python-queue/

from collections import deque

#List 를 queue 대용으로 사용이 가능함 FIFO 구조로
queue = [4,6,7,8,9]

queue.append(9)
queue.append(10)
print(queue) # [4, 6, 7, 8, 9, 9, 10]

print(queue.pop(0)) # 4
print(queue.pop(0)) # 6

print(queue) #[7, 8, 9, 9, 10]


# deque
# [list vs deque] https://wellsw.tistory.com/122
# append, appendleft, pop, popleft O(1)
# extend, extendleft -> O(N)
# rotate -> O(K)
queue = deque(queue) # deque([7, 8, 9, 9, 10])

queue.appendleft(11)
queue.appendleft(12)

print(queue)

# 오른쪽에다 넣음
queue.append(5)
queue.append(6)

print(queue)

# 왼쪽에서 뺌
queue.popleft()

# 오른쪽에서 뺌
queue.pop()

# extend 확장! 개수만큼 추가
target = [14,15,16]
queue.extend(target)
print(queue) #deque([11, 7, 8, 9, 9, 10, 5, 14, 15, 16])

# rotate 양옆으로 회전
queue.rotate(-1)
print(queue) #deque([7, 8, 9, 9, 10, 5, 14, 15, 16, 11])

queue.rotate(2)
print(queue) #deque([16, 11, 7, 8, 9, 9, 10, 5, 14, 15])