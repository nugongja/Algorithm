def solution(n, arr1, arr2):
    answer = []

    tmp = [[' ' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        code = arr1[i]

        j = 0
        while j < n:
            if code%2 == 1:
                tmp[i][n-j-1] = '#'
            code //= 2
            j+=1

        code = arr2[i]

        j = 0
        while j < n:
            if code%2 == 1:
                tmp[i][n-j-1] = '#'
            code //= 2
            j+=1

    for i in range(n):
        answer.append("".join(tmp[i]))
    

    return answer