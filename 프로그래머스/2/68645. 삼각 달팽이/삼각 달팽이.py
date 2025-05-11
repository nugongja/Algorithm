def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1,n+1)]

    cnt = n
    r = [1, 0, -1]
    c = [0, 1, -1]
    i = -1
    j = 0
    k = 1
    idx = 0

    while cnt > 0:
        for _ in range(cnt):
            i += r[idx]
            j += c[idx]
            answer[i][j] = k
            k += 1

        idx = (idx+1)%3
        cnt -= 1
    
    return [num for row in answer for num in row]