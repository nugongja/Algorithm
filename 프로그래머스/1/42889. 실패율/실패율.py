def solution(N, stages):
    user_total = len(stages)

    user_clear = [0]*(N+1)

    user_stop = [0]*(N+1)

    for stage in stages:
        if stage > N:
            stage = N
        else:
            user_stop[stage] += 1

        for i in range(1, stage+1):
            user_clear[i] += 1
    

    
    arr = [[0,i] for i in range(N+1)]


    for i in range(1, N+1):
        if user_clear[i] == 0:
            arr[i][0] = 0
        else:
            arr[i][0] = user_stop[i]/user_clear[i]
    
    arr = arr[1:]
    
    arr.sort(key=lambda x: (-x[0], x[1]))

    return list(arr[i][1] for i in range(N))