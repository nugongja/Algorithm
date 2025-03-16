def solution(n):
    tmp = ""

    while n != 0:
        tmp = str(n%3) + tmp
        n //= 3


    i = 0
    answer = 0
    for c in tmp:
        answer += int(c)*(3**i)
        i += 1

    return answer