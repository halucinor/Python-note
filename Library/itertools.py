# permutations https://wikidocs.net/109282
# combinations https://wikidocs.net/106964

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product

# 1. permutation
# 정해진 개수의 순열 반환
arr = ["A","B","C"]
nPc = permutations(arr) # iteration
nP2 = permutations(arr,2) # c = 2
print(list(nPc)) #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(list(nP2)) #[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 2. combination
# 정해진 개수의 조합 반환
data = ["A","B","C"] # 리스트 순서가 지켜짐
nCr = combinations(data,2) # r = 2
print(list(nCr)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 3. product
# 중복을 허용하는 순열
data = ["A","B","C"]
nPPc = product(data, repeat=2)
print(list(nPPc)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 4. combinations_with_replacement
# 중복을 허용하는 조합
data = ["A","B","C"]
nCCr = combinations_with_replacement(data, 2)
print(list(nCCr)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]