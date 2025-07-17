import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a,b)


def solution(arr):
    answer = 0

    a = arr.pop()
    while arr:
        b = arr.pop()
        a = lcm(a, b)

    return a
    