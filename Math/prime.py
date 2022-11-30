# 1보다 큰 수중 1과 자기 자신으로 밖에 나눠 떨어지지 않는 자연수

def is_prime(num):
    _sqrt = num ** 0.5
    _sqrt = int(_sqrt) + 1 # 제곱근 + 1까지 탐색
    
    if num == 1: 
        return False
    for i in range(2, _sqrt):
        if num % i == 0: return False
    return True

def prime_list(n):
    '''
    n : 소수를 찾는 범위
    return : 소수의 list
    '''

    sieve = [True] * (n+1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True: # i 가 소수이면
            for j in range(i + i, n + 1, i): # i 의 배수들을 False로
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]
