import sys 
sys.setrecursionlimit(10**6)

def dfs(Tree, Edge, node, visited, depth, minX, maxX):
    visited[node[2]] = True

    if depth == len(Tree):
        return


    for next in Tree[depth]:
        x, y, idx = next

        if visited[idx]:
            continue
        
        if minX < x < node[0]: # 왼
            Edge[node[2]][0] = idx
            dfs(Tree, Edge, next, visited, depth+1, minX, node[0])
        
        elif node[0] < x < maxX: # 오
            Edge[node[2]][1] = idx
            dfs(Tree, Edge, next, visited, depth+1, node[0], maxX)


    return Edge

def preorder(edge, node, order):
    if node == -1: return

    order.append(node+1)  # 루

    preorder(edge, edge[node][0], order) # 왼
    preorder(edge, edge[node][1], order) # 오

    return order


def postorder(edge, node, order):
    if node == -1: return

    postorder(edge, edge[node][0], order) # 왼
    postorder(edge, edge[node][1], order) # 오
    order.append(node+1)  # 루

    return order


def solution(nodeinfo):
    answer = [[], []]
    n = len(nodeinfo)

    for i, node in enumerate(nodeinfo):
        node.append(i)

    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    
    y = nodeinfo[0][1]+1

    Tree = []
    for node in nodeinfo:
        if y > node[1]:
            Tree.append([node])
            y = node[1]
        else:
            Tree[-1].append(node)

    Edge = [[-1, -1] for _ in range(n)]
    visited = [False]*n

    dfs(Tree, Edge, Tree[0][0], visited, 1, float('-inf'), float('inf'))

    preorder(Edge, Tree[0][0][2], answer[0])
    postorder(Edge, Tree[0][0][2], answer[1])
    
    return answer
