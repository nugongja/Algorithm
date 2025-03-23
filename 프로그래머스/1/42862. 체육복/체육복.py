def solution(n, lost, reserve):

    arr = [1]*(n+1)

    for i in reserve:
        arr[i] = 2
    
    for i in lost:
        arr[i] -= 1

    lost = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))

    answer = n - len(lost)


    for i in lost:
        if arr[i] == 0:
            if i - 1 > 0 and arr[i - 1] == 2:
                arr[i - 1] -= 1
                arr[i] += 1
                answer += 1
            elif i + 1 < n + 1 and arr[i + 1] == 2:
                arr[i + 1] -= 1
                arr[i] += 1
                answer += 1


    return answer