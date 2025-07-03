import sys
input = sys.stdin.readline


def solution(N, M):
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(i, cnt):
        nonlocal isExist
        visited[i] = True

        if cnt >= 5:
            isExist = True
            return 

        for next in graph[i]:
            if not visited[next]:
                dfs(next, cnt+1)

        visited[i] = False


    isExist = False
    for i in range(N):
        visited = [False]*N
        dfs(i, 1)
        if isExist:
            break

    if isExist:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
    

    