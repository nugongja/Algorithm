import sys
input = sys.stdin.readline
from collections import deque

def is_safe(room):
    for i in range(5):
        for j in range(5):
            if room[i][j] != 'P':
                continue
            q = deque()
            q.append((i, j, 0))
            visited = [[False]*5 for _ in range(5)]
            visited[i][j] = True
            
            while q:
                x, y, dist = q.popleft()
                if dist >= 3:
                    continue
                
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        if room[nx][ny] == 'P' and dist < 2:
                            return 0
                        if room[nx][ny] == 'O':
                            q.append((nx, ny, dist+1))
    return 1

def solution(places):
    answer = []

    for room in places:
        answer.append(is_safe(room))
                        
            

    return answer