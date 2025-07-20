import sys
from collections import deque
from math import inf
input = sys.stdin.readline

def Dikjstra(i, graph):
    answer = [inf]*len(graph)

    queue = deque()
    queue.append((0, i))
    answer[i] = 0

    while queue:
        curr_dist, curr_node = queue.popleft()

        for next_node in graph[curr_node]:
            next_dist = curr_dist + 1
            if next_dist < answer[next_node]:
                answer[next_node] = next_dist
                queue.append((next_dist, next_node))

    return answer


def solution(n, edge):

    graph = [[] for _ in range(n)]

    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)


    answer = Dikjstra(0, graph).count(max(Dikjstra(0, graph)))



    return answer