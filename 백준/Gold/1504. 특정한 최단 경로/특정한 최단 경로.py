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
        
        for next_node in range(1, V+1):
            next_dist = cur_dist + graph[cur_node][next_node]
            if next_dist < tmp[next_node]:
                tmp[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    
    return tmp


def solution():
    answer = inf
    V, E = map(int, input().split())

    graph = [[inf for _ in range(V+1)] for _ in range(V+1)]


    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
    v1, v2 = map(int, input().split())
    
    dist_from_1 = Dijkstra(graph, 1, V)
    dist_from_v1  = Dijkstra(graph, v1, V)
    dist_from_v2  = Dijkstra(graph, v2, V)

    answer = min(dist_from_1[v1]+dist_from_v1[v2]+dist_from_v2[V], dist_from_1[v2]+dist_from_v2[v1]+dist_from_v1[V])

    if answer == inf:
        answer = -1
    
    print(answer)

if __name__ == "__main__":
    solution()
    

    