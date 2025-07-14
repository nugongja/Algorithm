import sys
input = sys.stdin.readline



def solution(n, computers):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y:
            parent[root_y] = root_x



    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)



    answer = set(find(i) for i in range(n))

    return len(answer)
    