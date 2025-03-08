def solution(sizes):
    n = len(sizes)

    for i in range(n):
        sizes[i].sort()

    w = max(sizes[i][0] for i in range(n))
    h = max(sizes[i][1] for i in range(n))

    return w*h
