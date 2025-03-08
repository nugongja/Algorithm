def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)

    for i in range(n):
        schedules[i] += 10
        if schedules[i] % 100 >= 60:
            schedules[i] = (schedules[i]//100 + 1)*100 + ((schedules[i]-60)%100)
    
    for i in range(n):
        timelogs[i].pop(7-startday)  # 일요일
        timelogs[i].pop(6-startday)  # 토요일
        getPresent = True
        for log in timelogs[i]:
            if log > schedules[i]:
                getPresent = False
                break
        
        if getPresent:
            answer += 1

    return answer