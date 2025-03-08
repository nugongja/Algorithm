from collections import deque
import sys


def bfs(info, n, m):
    
    queue = deque()
    queue.append((0, 0, 0))
    visited = set()
    visited.add((0, 0, 0))

    answer = sys.maxsize

    while queue:
        a, b, depth = queue.popleft()

        if depth == len(info):
            if a < n and b < m:
                answer = min(answer, a)
            continue

        new_a, new_b = a+info[depth][0], b
        if(new_a, new_b, depth+1) not in visited:
            queue.append((new_a, new_b, depth+1))
            visited.add((new_a, new_b, depth+1))
        
        new_a, new_b = a, b+info[depth][1]
        if(new_a, new_b, depth+1) not in visited:
            queue.append((new_a, new_b, depth+1))
            visited.add((new_a, new_b, depth+1))

    
    return answer if answer != sys.maxsize else -1

def solution(info, n, m):
    return bfs(info, n, m)