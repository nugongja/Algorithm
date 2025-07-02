
import sys
import heapq

def solution(V,E,K):
    answer = [sys.maxsize]*(V+1)
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))
    

    pq = []
    heapq.heappush(pq, (0, K))
    answer[K] = 0

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > answer[cur_node]:
            continue

        for w, next_node in graph[cur_node]:
            next_dist = cur_dist + w
            if next_dist < answer[next_node]:
                answer[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    
    return answer

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    answer = solution(V,E,K)
    for i in range(1, V + 1):
        print("INF" if answer[i] == sys.maxsize else answer[i])

    