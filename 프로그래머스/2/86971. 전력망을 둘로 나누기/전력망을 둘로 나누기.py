import sys
input = sys.stdin.readline


def solution(n, wires):
    def dfs(a):
        cnt = 1
        visited[a] = True

        for next in graph[a]:
            if not visited[next]:
                cnt += dfs(next)

        return cnt

    
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)


    answer = 100
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        visited = [False]*(n+1)
        k1 = dfs(v1)
        k2 = dfs(v2)
        answer = min(answer, abs(k1-k2))


        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer