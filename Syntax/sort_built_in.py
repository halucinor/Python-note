'''
- list.sort()
- sorted()
- string 정렬
- reverse
- tuple dict sort -> 첫번째 항목 비교 그 다음 두번째
'''

# List In place 정렬
a = [5, 2, 3, 1, 4]
a.sort()
print(a) # [1,2,3,4,5]

# List sorted
b = [7,5,9,9,4,3,1,47,5]
sorted_b = sorted(b)
print(b) # [7, 5, 9, 9, 4, 3, 1, 47, 5]
print(sorted_b) # [1, 3, 4, 5, 5, 7, 9, 9, 47]

# String 정렬
## 대문자 먼저 정렬됨
some_string = list("TheQuickBrownFoxJumpsOverTheLazyDog") # 문자열 하나씩 자르기
some_string.sort() # 다음 줄 부터 적용됨
sorted(some_string) # 바로 적용
#print(some_string)

## 대소문자 구분 X 정렬
sorted_str = sorted("This is a test string from Andrew".split(), key=str.lower) #str.upper
print(sorted_str) # ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# reverse
a.reverse()
print(a) # [5, 4, 3, 2, 1]

# sorted , reverse true
print(sorted(b, reverse=True)) # [47, 9, 9, 7, 5, 5, 4, 3, 1]
reversed_str = sorted(sorted_str, reverse=True, key = str.lower) 
print(reversed_str) # ['This', 'test', 'string', 'is', 'from', 'Andrew', 'a']

# reversed -> 이터레이터 생성
bb = reversed(b)
print(bb) # reverseiterator
for item in bb:
    print(item, end = ',')
else:
    print()

# tuple sort
tuple_a = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(tuple_a)) # 첫번째 먼저 정렬 후 두번째 정렬 [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

# dict sort
dict_bb = {key:item for item, key in enumerate(list("zywdowjpocjpoawbef"))}
print(sorted(dict_bb)) # key 만 정렬 ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'o', 'p', 'w', 'y', 'z']
print(sorted(dict_bb.items())) 
# key 기준 정렬 
# [('a', 13), ('b', 15), ('c', 9), ('d', 3), ('e', 16), ('f', 17), ('j', 10), ('o', 12), ('p', 11), ('w', 14), ('y', 1), ('z', 0)]

# https://docs.python.org/ko/3/howto/sorting.html
