'''TOC
- for-if-else
- for 반대로 실행

'''
# for-else 문은 중간에 break 되지 않고 마지막 요소까지 반복했을 때 수행

print('#1. for-else test')
for i in range(10):
    # print(i)
    if i == 5:
        break
else:
    print('for is not breaked')

''' Result
# Nothing printed
'''

print("#2. for-else test(2)")
for i in range(10):
    if i == 11:
        break
else:
    print('for is not breaked')

''' Result
# for is not breaked
'''

##############################

# for 문 반대로 실행
for i in range(10,0,-1): # 10 ~ 1
    ...

for i in reversed(range(10)): # 9 ~ 0 부터 시작
    ...

