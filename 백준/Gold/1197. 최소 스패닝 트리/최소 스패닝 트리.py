import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq


def prim(n, graph):
    visited = [False]*n
    min_heap = []
    total_cost = 0

    visited[0] = True
    for cost, next_node in graph[0]:
        heapq.heappush(min_heap, (cost, next_node))

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        
        visited[node] = True
        total_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_cost, next_node))
    

    return total_cost


def solution():
    V, E = map(int, input().split())

    graph = [[] for _ in range(V)]


    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A-1].append((C, B-1))
        graph[B-1].append((C, A-1))

    answer = prim(V, graph)

    return answer
    

if __name__ == "__main__":
    a = solution()
    print(a)
