''' TOC
- List comprehension
- Split and join
- enumerate and zip
'''

### List comprehension

# 같은 숫자는 싫어 : https://school.programmers.co.kr/learn/courses/30/lessons/12906
arr = [1,1,3,3,0,1,1]

answer = [arr[0]] + [ele for i, ele in enumerate(arr) if i != 0 and arr[i-1] != arr[i]]
# [1,3,0,1]

# 다음과 같이 표현 가능
# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#         for 항목2 in 반복가능객체2 if 조건문2
#         ...
#         for 항목n in 반복가능객체n if 조건문n]

#----------------------------------------------------------------------------------------#
### split
items = 'zero one two three'.split() # 빈칸 기준 문자열 나누기
example = 'python,java,javascript'.split(',') # 쉼표(,) 기준 문자열 나누기

print("items ", items) # ['zero', 'one', 'two', 'three']
print('example', example) # ['python', 'java', 'javascript']

#----------------------------------------------------------------------------------------#

### unpacking
unpack = 'team,ai,deeplearning'
team, ai, deeplearning = unpack.split(',')
print(team, ai, deeplearning)# team ai deeplearning
#----------------------------------------------------------------------------------------#

### join
colors = ['red','blue','green','yellow']
result = ' '.join(colors) 
print(result) # red blue green yellow

#----------------------------------------------------------------------------------------#

### enumerate

#example 1
tic_tac_toe = ['tic', 'tac', 'toe']

for index, value in enumerate(tic_tac_toe):
  print(index, value)
# 0 tic
# 1 tac
# 2 toe

#example 2
my_list = ['a', 'b', 'c', 'd']
print(list(enumerate(my_list))) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

#example 3
dic = {i:j for i, j in enumerate("The Quick Brown Fox Jumps Over The Lazy Dog".split())}
print(dic) # {0: 'The', 1: 'Quick', 2: 'Brown', 3: 'Fox', 4: 'Jumps', 5: 'Over', 6: 'The', 7: 'Lazy', 8: 'Dog'}
#----------------------------------------------------------------------------------------#

### zip
a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for a, b in zip(a_list, b_list):
  print(a, b)
# a1 b1
# a2 b2
# a3 b3


c_list = ['c1', 'c2', 'c3', 'c4'] #길이가 다르면?
for a, c in zip(a_list, c_list):
  print(a,c)
# a1 c1
# a2 c2
# a3 c3


### enum & zip 동시사용
for i , (a,b) in enumerate(zip(a_list, b_list)):
  print(i, a, b)

# 0 a1 b1
# 1 a2 b2
# 2 a3 b3