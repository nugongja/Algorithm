def solution(a, b, n):
    answer = 0

    tmp = 0
    while True:
        if n < a:
            break
        if(n//a > 0):
            answer += (n//a)*b
            n = (n//a)*b + n%a
            



    return answer

