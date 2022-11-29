'''
- for-if-else
- 삼항 연산
- where
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

