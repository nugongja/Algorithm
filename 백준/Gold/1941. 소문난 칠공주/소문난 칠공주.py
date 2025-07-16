import sys
input = sys.stdin.readline
import itertools
from collections import deque


def isconnected(selected):
    visited = [False]*7

    queue = deque([0])
    visited[0] = True
    cnt = 1

    while queue:
        idx = queue.popleft()
        curr_r, curr_c = selected[idx]

        for i in range(7):
            if not visited[i]:
                next_r, next_c = selected[i]

                if abs(curr_r-next_r) + abs(curr_c-next_c) == 1:
                    cnt += 1
                    visited[i]=True
                    queue.append(i)

    return cnt == 7

def solution():
    answer = 0
    board = [list(input().strip()) for _ in range(5)]

    
    for comb in itertools.combinations(range(25), 7):
        selected = [(i//5, i%5) for i in comb]
        s_count = sum(1 for x, y in selected if board[x][y] == 'S')

        if s_count >= 4 and isconnected(selected):
            answer += 1
    
 
    print(answer)
                



if __name__ == "__main__":
    solution()