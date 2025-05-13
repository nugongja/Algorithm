def binary(n):
    tmp = 0
    while n > 0:
        tmp = tmp+1 if n%2 == 1 else tmp
        n //= 2
    
    return tmp

def solution(n):
    answer = 0

    tmp = binary(n)
    for i in range(n+1, 1000001):
        if binary(i) == tmp:
            answer = i
            break
    

    return answer