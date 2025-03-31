def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        answer.append([])
        for p, q in zip(i, j):
            answer[-1].append(p+q)

    return answer