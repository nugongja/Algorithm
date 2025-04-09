def solution(n):
    arr = [1]*(n+1)
    for i in range(2, n+1):
        if arr[i] == 1:
            for j in range(i+i, n+1, i):
                arr[j] = 0

    return sum(arr)-2