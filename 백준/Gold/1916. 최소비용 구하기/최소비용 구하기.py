import sys
import heapq
from math import inf
input = sys.stdin.readline

def Dijkstra(graph, K, V):
    tmp = [inf]*(V+1)

    tmp[K] = 0
    pq = [(0, K)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > tmp[cur_node]:
            continue
        
        for w, next_node in graph[cur_node]:
            next_dist = cur_dist + w
            if next_dist < tmp[next_node]:
                tmp[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    
    return tmp


def solution(N, M):
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w,v))

    
    start, end = map(int, input().split())

    answer = Dijkstra(graph, start, N)[end]

    
    print(answer)

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    solution(N, M)
    

    