import sys
import heapq
from math import inf
input = sys.stdin.readline

def solution(V,E,K):
    answer = [inf]*(V+1)
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
    

    answer[K] = 0
    pq = [(0, K)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > answer[cur_node]:
            continue

        for w, next_node in graph[cur_node]:
            next_dist = cur_dist + w
            if next_dist < answer[next_node]:
                answer[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    for i in range(1, V + 1):
        print("INF" if answer[i] == inf else answer[i])
    

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    solution(V,E,K)