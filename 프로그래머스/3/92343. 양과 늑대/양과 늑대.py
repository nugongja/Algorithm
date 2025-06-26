def solution(info, edges):
    from collections import defaultdict

    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    max_sheep = 0

    def dfs(cur, sheep, wolf, next_nodes):
        nonlocal max_sheep

        if info[cur] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        for i, next_node in enumerate(next_nodes):
            new_next = next_nodes[:i] + next_nodes[i+1:] + tree[next_node]
            dfs(next_node, sheep, wolf, new_next)

    dfs(0, 0, 0, tree[0])    

    return max_sheep
