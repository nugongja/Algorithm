def solution(X, Y):
    answer = ''
    X = list(map(int, X))
    Y = list(map(int, Y))
    

    arr = []
    for i in range(9, -1, -1):
        tmp = min(X.count(i), Y.count(i))
        if tmp > 0:
            if len(arr) == 0 and i == 0: tmp = 1
            arr.append((i, tmp))

    arr.sort(reverse=True)
    
    if len(arr) == 0:
        answer = "-1"
    else:    
        for value, cnt in arr:
            answer += str(value)*cnt



    return answer