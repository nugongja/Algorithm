import math
from itertools import combinations

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def solution(nums):
    answer = 0

    sumOf3 = [sum(comb) for comb in combinations(nums, 3)]
    
    for s in sumOf3:
        if(isPrime(s)):
            answer += 1

    return answer