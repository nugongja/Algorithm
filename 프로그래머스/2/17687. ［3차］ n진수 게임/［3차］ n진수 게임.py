import sys
input = sys.stdin.readline

def tenToN(i, n):
        characters = '0123456789ABCDEF'

        if i == 0:
            return '0'

        tmp = ''
        while i > 0:
            tmp = characters[i%n] + tmp
            i //= n
        
        return tmp



def solution(n, t, m, p):

    s = ''
    i = 0
    # # 튜브가 말해야 할 위치들을 안전하게 커버함 (총 t개를 말하고, 말할 위치는 m 간격으로 점프)
    while len(s) < t*m:  
         s += tenToN(i, n)
         i += 1

    # p-1: 튜브의 시작 인덱스, m: 한 바퀴마다 돌아오는 순서 간격, t: 말해야 할 횟수
    return s[p-1::m][:t]  
