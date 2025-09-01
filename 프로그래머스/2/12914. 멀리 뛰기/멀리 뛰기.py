import sys
input = sys.stdin.readline
from math import comb


def solution(n):
    answer = 0

    one = n
    two = 0
    while one >= 0:
        answer += comb(one+two, two)
        one -= 2
        two += 1


    return answer%1234567