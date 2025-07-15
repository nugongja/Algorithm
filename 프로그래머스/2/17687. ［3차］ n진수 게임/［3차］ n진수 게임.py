import sys
input = sys.stdin.readline

def solution(n, t, m, p):

    def tenToN(i, n):
        tmp = ''

        if i == 0:
            return '0'

        while i > 0:
            tmp = characters[i%n] + tmp
            i //= n
        
        return tmp


    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


    string = ''
    i = 0
    while len(string) < p+(t-1)*m:
        temp = tenToN(i, n)
        string += temp
        i += 1


    answer = ''
    cnt = 0
    while cnt != t:
        answer += string[(p-1)+cnt*m]
        cnt += 1
   

    return answer
