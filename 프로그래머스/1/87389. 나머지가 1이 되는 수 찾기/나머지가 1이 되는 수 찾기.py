def solution(n):
    answer = 0

    n -= 1
    for i in range(2, n+1):
        if n%i == 0:
            answer = i
            break

    return answer
