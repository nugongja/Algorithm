def solution(players, m, k):
    answer = 0

    for i in range(24):
        if players[i]//m > 0:
            answer += players[i]//m
            players[i:min(i+k, 24)] = map(lambda p: p - m*(players[i]//m), players[i:min(i+k, 24)])
            

    return answer
        