def solution(food):
    answer = ''
    n = len(food)

    for i in range(1, n):
        food[i] //= 2
    
    tmp = ''
    tmp_reversed = ''
    for i in range(1, n):
        tmp += (str(i))*food[i]
        tmp_reversed += str(n-i)*food[n-i]
    
    answer = tmp + '0' + tmp_reversed
    return answer
