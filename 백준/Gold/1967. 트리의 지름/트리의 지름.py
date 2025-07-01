from collections import deque
import itertools

def getLeafNodes(arr):
    visited = [False]*len(arr)

    for i in range(len(arr)-1, 0, -1):
        visited[arr[i]] = True
    visited[0] = True

    leafs = []
    for i in range(len(arr)):
        if not visited[i]:
            leafs.append(i)
    
    return leafs

def solution(N):
    answer = 0

    weight_to_parent = [0]*N
    parent = [-1]*N
    children = [0]*N
    for _ in range(N-1):
        p, c, w = map(int, input().split())
        weight_to_parent[c-1] = w
        parent[c-1] = p-1
        children[p-1] += 1
    
    leafs = getLeafNodes(parent)

    max_paths  = [[] for _ in range(N)] # 각 노드마다 (왼쪽 path의 최댓값오른쪽 path의 최댓값)저장
    
    
    queue = deque(leafs)
    visited = [False]*N
    for leaf in leafs:
        visited[leaf] = True
        max_paths[leaf] = [0,0]
    
    while queue:
        now = queue.popleft()

        p = parent[now]
        
        if len(max_paths[now]) == children[now]:
            for tmp in itertools.combinations(max_paths[now], min(children[now], 2)):
                answer = max(answer, sum(tmp))


        max_paths_to_parent = max(max_paths[now]) + weight_to_parent[now]
        if p != -1:
            max_paths[p].append(max_paths_to_parent)
        
            if not visited[p] and len(max_paths[p]) == children[p]:
                visited[p] = True
                queue.append(p)

    
    return answer

if __name__ == "__main__":
    N = int(input())
    answer = solution(N)
    print(answer)

    


