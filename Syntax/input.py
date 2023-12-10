# https://itcrowd2016.tistory.com/81

# 한줄로 읽어서 정수로 변환
N = int(input())
print(N)
## input : 10

# N개의 정수를 한줄로 입력받을 경우
line = input().split()
print(line)
## input: 10 20 30

# N개의 정수를 list로 저장할 경우
line = input().split()
data = list(map(int, line))

# N개의 정수를 여러 줄에 걸쳐 입력받아 이차원 배열에 저장할 경우
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

## sys.stdin.readline()
import sys

# N개의 정수를 한 줄로 입력 받을 경우
read = sys.stdin.readline
N, M, K = map(int, read().split())

# N개의 정수를 list로 저장할 경우
read = sys.stdin.readline
data = list(map(int, read().split()))

# N개의 정수를 여러줄에 걸쳐 입력받아 List에 저장하는 경우
read = sys.stdin.readline
N = int(read())
data = [int(read()) for _ in range(N)]

# 5 -> N
# 5
# 4
# 3
# 2
# 1

# N개의 정수를 여러 줄에 걸쳐 입력받아 이차원 배열에 저장할 경우
read = sys.stdin.readline
N = int(read())
mat = [list(map(int, read().split())) for _ in range(N)]

# 4
# 1 2 3
# 3 2 4
# 5 6 7
# 7 8 9

