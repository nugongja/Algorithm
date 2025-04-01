def solution(num):
    answer = 0

    x = num
    while x != 1:
        if x%2 == 0:
            x //= 2
        else:
            x = x*3 + 1

        answer += 1
    
    if answer > 500:
        answer = -1

    return answer