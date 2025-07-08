import sys
input = sys.stdin.readline
from collections import deque


def solution():
    N, M = map(int, input().split())

    answer = [1]*N
    parent = [[] for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        parent[B-1].append(A-1)



    # 선수 과목은 i보다 인덱스가 작을 수 밖에 없음
    for i in range(N):
        for p in parent[i]:
            answer[i] = max(answer[p]+1, answer[i])

    


    for k in answer:
        print(k, end=' ')

if __name__ == "__main__":
    solution()
    

    