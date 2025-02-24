def get_divisors(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    
    return cnt


def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        tmp = get_divisors(i)
        print(tmp)
        if tmp > limit:
            answer += power
        else:
            answer += tmp

    
    return answer
