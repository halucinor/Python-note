# https://www.daleseo.com/python-collections-counter/

from collections import Counter

alpha = list("hiheyhihihellohey")
counter = Counter(alpha) # Counter({'h': 6, 'i': 3, 'e': 3, 'y': 2, 'l': 2, 'o': 1})

# dict 처럼 사용 가능
print(counter["h"]) # 6

# iteration 가능
for item in counter.items():
    print(item)

# 가장 흔한 데이터 찾기
# list 형태로 정렬하여 return
most_common = counter.most_common() 
print(most_common) # [('h', 6), ('i', 3), ('e', 3), ('y', 2), ('l', 2), ('o', 1)]

# 산술 연산자
counter1 = Counter(["A", "A", "B"])
counter2 = Counter(["A", "B", "B"])

counter3 = counter1 + counter2
print(counter3) # Counter({'A': 3, 'B': 3})

counter4 = counter1 - counter2
print(counter4) # Counter({'A': 1})

# 누적하기
counter = counter1 # Counter({'A': 2, 'B': 1})
counter.update(["A","B","B","B","C","C","C","D"])
print(counter) # Counter({'B': 4, 'A': 3, 'C': 3, 'D': 1})

# 가장 흔한 n 개 출력
most_common_2 = counter.most_common(2) #[('B', 4),('A', 3)]
print(most_common_2)