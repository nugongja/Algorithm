import sys
input = sys.stdin.readline
from collections import deque

def solution(people, limit):
    answer = 0

    queue = deque(sorted(people, reverse=True))

    while queue:
        if len(queue) == 1:
            answer += 1
            break

        big = queue.popleft()
        small = queue.pop()

        if big+small > limit:
            queue.append(small)
        
        answer += 1


    return answer
