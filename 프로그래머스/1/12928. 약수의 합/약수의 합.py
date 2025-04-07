import math

def solution(n):
    answer = 0

    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            print(i, int(n/i))
            answer += (i + int(n/i))
        
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        answer -= int(math.sqrt(n))

    return answer
