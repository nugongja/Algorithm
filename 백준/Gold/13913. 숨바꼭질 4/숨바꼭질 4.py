from collections import deque

def solution(N, K):
    visited = [False]*100001
    prev = [-1]*100001

    q = deque()
    q.append(N)

    while q:
        curr = q.popleft()

        if curr == K:
            break

        for move in [-1,1,curr]:
            next = curr + move
            if 0 <= next <= 100000 and not visited[next]:
                q.append(next)
                visited[next] = True
                prev[next] = curr
    

    path = []
    curr = K
    while curr != N:
        path.append(curr)
        curr = prev[curr]


    return path

if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = solution(N, K)
    print(len(answer))
    print(str(N) + ' ' + ' '.join(map(str, reversed(answer))))

    

