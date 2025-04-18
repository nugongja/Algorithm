import math

def solution(r1, r2):

    answer = 0
    for i in range(r2+1):
        max_y = math.floor((r2**2 - i**2)**0.5)
        min_y = math.ceil((r1**2 - i**2)**0.5) if i <= r1 else 0
        answer += (max_y - min_y) + 1
    
    print(r2-r1+1)
    return answer*4 - (r2-r1+1)*4
