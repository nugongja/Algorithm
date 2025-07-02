
import sys
from queue import PriorityQueue

def solution(V,E,K):
    answer = [sys.maxsize]*(V+1)

    # 간선
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))
    
    for i in range(1, V+1):
        graph[i] = sorted(graph[i])

    pq = PriorityQueue()
    pq.put((0, K))
    answer[K] = 0

    while pq.qsize() != 0:
        cur_dist, cur_node = pq.get()

        for w, next_node in graph[cur_node]:
            next_dist = cur_dist + w
            if next_dist < answer[next_node]:
                answer[next_node] = next_dist
                pq.put((next_dist, next_node))

    
    return answer

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    answer = solution(V,E,K)
    for i in range(1, V+1):
        if answer[i] == sys.maxsize:
            print("INF")
        else:
            print(answer[i])

   