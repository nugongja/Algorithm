import math

def numberOfDivisor(N):
    cnt = 0
    for i in range(1, int(math.sqrt(N))+1):
        if i*i == N: cnt += 1
        elif N%i == 0: cnt += 2
    return cnt

def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        tmp = numberOfDivisor(i)
        if tmp%2 == 0:
            answer += i
        else:
            answer -= i

    return answer  