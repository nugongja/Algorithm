def solution(d, budget):
    answer = 0

    d = sorted(d)

    idx = 0
    while(budget - d[idx] >= 0):
        budget -= d[idx]
        idx += 1
        if idx >= len(d):
            break
        
        
    return idx
