import sys
import heapq

def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n+1)]
    cost = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))


    for start in range(1, n+1):
        hq = [(0, start)]
        cost[start][start] = 0

        while hq:
            cur_cost, u = heapq.heappop(hq)
            if cur_cost > cost[start][u]:
                continue
            for v, w in graph[u]:
                if cost[start][v] > cost[start][u] + w:
                    cost[start][v] = cost[start][u] + w
                    heapq.heappush(hq, (cost[start][v], v))


    answer = cost[s][a] + cost[s][b]

    for i in range(1, n+1):
        answer = min(answer, cost[s][i] + cost[i][a] + cost[i][b])
            

    return answer
