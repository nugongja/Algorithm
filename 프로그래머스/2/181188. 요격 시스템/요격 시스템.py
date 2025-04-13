def solution(targets):
    answer = 0

    targets.sort(key=lambda x:x[1])
    
    last_shot = -float('inf')

    for s, e in targets:
        if last_shot <= s:
            answer += 1
            last_shot = e - 0.1



    return answer