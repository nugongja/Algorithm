def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)

    for i in range(n):
        schedules[i] += 10
        schedules[i] += 40 if schedules[i] % 100 >= 60 else 0

    for i in range(n):
        answer += all(
            log <= schedules[i]
            for j, log in enumerate(timelogs[i])
            if j != (6-startday+7)%7 and j != 7-startday)
        
        

    return answer