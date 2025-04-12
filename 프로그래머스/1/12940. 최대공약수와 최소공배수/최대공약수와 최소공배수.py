def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b>0:
        tmp = b
        b = a%b
        a = tmp
    
    return a

def solution(n, m):

    return [gcd(n, m),(n*m)//gcd(n, m)]