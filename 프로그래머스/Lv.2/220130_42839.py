from math import sqrt
from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = sorted(list(numbers), reverse=True)
    permutated = set()
    for i in range(1, len(numbers)+1):
        permutated |= set(map(lambda x: int(''.join(x)), list(permutations(numbers, i))))
    
    for p in list(permutated):
        if isPrime(p): print(p); answer +=1
        
    return answer
        
def isPrime(num):
    if num == 2: return True
    elif num in [0, 1]: return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True
print(solution("011"))