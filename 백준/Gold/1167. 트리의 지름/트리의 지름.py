import sys
input = sys.stdin.readline
import heapq
from math import inf

def Dikjstra(graph, i):
    dist = [inf]*len(graph)
    dist[i] = 0

    hq = []
    heapq.heappush(hq, (0, i))


    while hq:
        curr_dist, curr_node = heapq.heappop(hq)

        for next_weight, next_node in graph[curr_node]:
            next_dist = curr_dist + next_weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(hq, (next_dist, next_node))



    return dist
    


def solution():
    V = int(input())
    graph = [[] for _ in range(V)]

    for _ in range(V):
        line = list(map(int, input().split()))
        idx = 0
        v = line[idx]-1

        idx += 1
        while line[idx] != -1:
            graph[v].append((line[idx+1], line[idx]-1))
            idx += 2
            

    endpoint_1 = -1

    dist_from_0 = Dikjstra(graph, 0)
    max_tmp = 0
    for i in range(V):
        if dist_from_0[i] != inf and dist_from_0[i] > max_tmp:
            max_tmp = dist_from_0[i]
            endpoint_1 = i

    
    dist_from_endpoint_1 = Dikjstra(graph, endpoint_1)
    max_length = 0
    for i in range(V):
        if dist_from_endpoint_1[i] != inf and dist_from_endpoint_1[i] > max_length:
            max_length = dist_from_endpoint_1[i]


        
    print(max_length)


if __name__ == "__main__":
    solution()
    
