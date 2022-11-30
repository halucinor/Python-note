# list 인덱실, 슬라이싱 https://wikidocs.net/16037
'''
    list indexing
    list sliceing
'''

s = [0,1,2,3,4,5,6,7,8,9,10] # 11개

# indexing
print(s[0]) # 0
print(s[5]) # 5

print(s[-1]) # 10
print(s[-5]) # 6

# sliceing
# 리스트변수[시작인덱스:종료인덱스:step]
ss = s[0:3] # start ~ end-1 까지
print(ss) #[0, 1, 2]

# 음수도 가능
print(s[0:-2]) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 처음부터 끝까지
print(s[:])
a = s[:] # -> copy

# 특정위치부터 종료인덱스 까지
print(a[3:]) # [3, 4, 5, 6, 7, 8, 9, 10]

# 처음부터 특정위치까지
print(a[:3]) # [0, 1 , 2]


# step
print(a[0:5:2]) # [0, 2, 4]
print(a[0::2]) #[0, 2, 4, 6, 8, 10]

# step 응용 거꾸로 바꾸기
print(a[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a[::-2]) # [10, 8, 6, 4, 2, 0]
