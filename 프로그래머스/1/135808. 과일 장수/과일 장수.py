def solution(k, m, score):
    answer = 0
    n = len(score)

    score.sort(reverse=True)
    
    i = m-1
    while i < n:
        answer += (score[i]*m)
        i += m
        

    return answer

    