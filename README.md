# Python-note
- 유용한 알고리즘에 대한 참고 노트 및 library
- 문제 풀이에 관한 Template 및 접근 방법에 대한 정리

## Syntax
- **Loop and Condition**
  - [for-if](./Syntax/Loop_and_condition.py)
  - [Pythonic Code](./Syntax/Pytonic_code.py)

- **Python Sort**
  - [다양한 sort 구현](./Syntax/Sorting.py)
  - [library](./Syntax/[TODO])
  - [Custom sort](./Syntax/cmp_to_key.py)
    
- **String Handling**
  - Sliceing and Indexing
  - regex
    
- **Dict**
    Initilization
    Sorting

- **Data Structure**
    Collections

- **Matrix handling**
  - [90-degree Matrix rotation](./Library/matrix_rotation.py)
  - [Matrix Rotation](./Library/[TODO])

- **Math**  
Math library
Permutation, Combination  
LCM, GCD   
Check Prime Number  
Find All Divisors  
Prime Factorization
에라토스테네스의 채

## 알고리즘 유형에 따른 Tip 

### 그리디

문제를 가장 쉽게 접근하는 방법 중에 하나이지만, 그리디로 풀리는지 증명하는 과정이 매우 어렵다.
그리디 알고리즘을 적용하기전에, 그렇게 해도 최적의 해가 보장되는지 증명하고 접근하는 것이 좋다.
문제를 보았을 때, 초기에 DP와 Greedy 유형을 헷갈리기 쉽다.

### Binary search, parametric search

- 문제에서 어떤 조건을 만족시키는 최대, 최소값을 찾기
- 탐색 범위가 1억 ~ 10억 이상이면 이분탐색의 가능성을 의심

```python
#이분탐색 template  
left = 0
right = 10 ** 10 #some large number
result = 0
while left <= right:

    mid = (left + right) // 2
            
    if is_possible(mid): # <- 높은 값 탐색 
        answer = mid # min(answer, mid)
        left = mid + 1
    else: # <- 낮은 값 탐색
        right = mid - 1
```

- biselect


### BFS/DFS

너비우선탐색(Breadth First Search, BFS).  
그래프문제나 격자판이 주어진 상황에서 경로를 찾는 문제에서 자주 사용되지만, 매 순간에 선택지를 만드는 순간에도 잘 사용!!
BFS/DFS/Dijkstra 는 코테에서 자주 등장
큐를 사용하는 BFS나 Dijkstra에서는 큐에 삽입되는 원소가 중요한데, 어느 순간의 상태를 큐에 저장한다고 생각하면 어떻게 튜플을 구성해서 큐에 삽입해야 하는지 쉽게 설정할 수 있다.
예시: (현재위치, 이동횟수, 이동방향, 남은 스킬 사용횟수, etc..) 들을 묶어서 큐에 삽입 가능
마찬가지로 방문처리도 거의 설정한 튜플의 크기만큼 지정해서 방문을 확인한다.

```
q = [start]
vis[start] = true

while q:
  here = q.pop(0) #deque 사용시 popleft()
  
  for there in adj[here]:
    if vis[there]: continue
    q.push(there)
```    

깊이우선탐색(Depth First Search, DFS)

```
def dfs(here):
  vis[here] = true
  for there in adj[here]:
    if vis[there]: continue
    dfs(there)
```
### Dijstra
### Floyd–Warshall algorithm
### Minimum Spanning Tree (MST)
### Topology Sort
### BackTracking
### 누적합
### Bitmasking

비트마스킹(Bitmask)
입력으로 주어지는 수나 특정 조건의 범위가 10 이하로 매우 작다면 사용을 의심해볼 수 있다.
어떤 상태를 저장하기에 매우 용이하고, 응용하여 가능한 모든 조합을 탐색하는 방법에도 사용할 수 있다.
비트마스킹의 장점은 단 하나의 수만으로 여러 상태를 저장할 수 있는 것!!
# 예를 들어 8개의 전구가 있고 2번째, 5번째 전구가 켜져있는 상태를 표시하고 싶다면

bulb_status = 0 # 초기상태 (모든 전구가 꺼짐)     0000 0000
bulb_status |= (1 << 2) # 2 번째 전구 ON         0000 0100
bulb_status |= (1 << 5) # 5 번째 전구 ON         0010 0100

### Divid and Cunquer 
### Disjoint-Set (Union-Find)
### Two Pointer
### Dynamic Programming
문제를 풀고 해결방법을 구상하다가 중복되는 연산이 자주 등장하거나, 어떤 상태를 만족하기 이전 상태에서도 최적의 상태를 만족해야할 때 사용

그리디 알고리즘과 동적계획법 둘 중에 어떤 것을 사용해야하는지 감이 잡히지 않을 때

문제의 풀이 방법이 증명 가능하며, 중복된 연산이 많이 등장하지 않는 경우: 그리디 알고리즘
문제의 풀이 방법에 대한 증명이 잘 떠오르지 않고, 중복되는 연산이 여러번 등장하는 경우: 동적계획법
감이 잡히지 않을 때는, 가장 기초 문제부터 많은 양의 문제를 풀며 생각하는 힘을 기르는 것이 좋다 😄

동적계획법 중에서도 유명한 문제유형들 (Knapsack problem, LIS(Longest Increaseing Subsequence), LCS(Longest Common Subsequence), 외판원순회문제(TSP)) 은 따로 익히는 것이 좋다. 특히 LIS, LCS, 냅색문제는 잘 나오기 때문에 확실하게 알고있는 것이 문제를 풀 때 도움이 된다.

LIS 알고리즘의 경우, 동적계획법을 이용한 풀이와, 이분탐색을 이용한 풀이 2가지 방법이 모두 존재하므로 모두 알아두고 있으면 좋다

아직 많은 코딩테스트를 참여하지는 않았지만, 개인적으로 문제를 풀면서 유명한 DP알고리즘을 적용한 문제보다는 직접 점화식을 생성하는 문제가 더 자주 등장하는 것 같음!

# 1. 재귀를 사용한 Top Down 방법

memo = [[-1] * N for _ in range(N)]

# 완전탐색을 하되, 이미 연산한 부분에 대해서는 가지치기를 진행하는 방법
# N의 크기가 너무 커지면 python에서는 재귀호출 횟수제한에 걸려서 오류가 발생할 수 있음!
# 처음에 완전탐색으로 생각을 시작해서 최적화하기에 좋은 코드!

def dp(n):
# 기저사례 (base condition)
if n <= 1: return n

# 메모이제이션 (memoization)
if memo[n] != -1: return ret

# 재귀연산
memo[n] = dp(n - 1) + dp(n - 2)
return memo[n]

# 2. Bottom Up 방법
# 단순 반복문을 사용하는 방법이지만, 점화식을 세워 그대로 적용시켜야한다.
memo = [0] * N
memo[1] = 1
for i in range(2, N):
  memo[i] = memo[i - 2] + memo[i - 1] 
# 이런 상태들을 저장하는데 단 하나의 숫자형 변수를 사용!

## TBD
Bipartite Matching
Tree
Line
Plane
KMP
Trie
Tiling Problem
0-1 Knapsack Problem
LIS (Longest Increasing Subsequence)
LCS (Longest Common Subsequence)
Matrix Chain Multiplication
Geometry
Number of intersection points of two lines in 1 dimension
CCW
Convex Hull
Polygon
Probability Theory
Signal Processing
FFT
Miscellaneous
Number of intervals whose sum is M
Interval Sum
Prefix Sum
Fenwick Tree (Binary Indexed Tree)
Handling Recursion Limit