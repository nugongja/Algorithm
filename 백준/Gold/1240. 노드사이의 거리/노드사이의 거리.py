import sys
input = sys.stdin.readline
from math import inf
import heapq

def Dikjstra(start, n, graph):
    min_heap = []
    cost = [inf]*n

    heapq.heappush(min_heap, (0, start))

    while min_heap:
        now_cost, now_node = heapq.heappop(min_heap)

        for next_weight, next_node in graph[now_node]:
            next_cost = now_cost + next_weight
            
            if next_cost < cost[next_node]:
                cost[next_node] = next_cost
                heapq.heappush(min_heap, (next_cost, next_node))
    
    return cost



def solution():

    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a-1].append((c, b-1))
        graph[b-1].append((c, a-1))
    
    cost = [[] for _ in range(N)]
    for i in range(N):
        cost[i] = Dikjstra(i, N, graph)
    
    for _ in range(M):
        a, b = map(int, input().split())
        print(cost[a-1][b-1])


    

if __name__ == "__main__":
    solution()
