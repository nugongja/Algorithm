def solution(sequence, k):
    answer = [0, 1000000]

    i = 0
    j = -1
    tmp = 0
    while i < len(sequence) and j < len(sequence):
        if tmp == k:
            if j - i + 1 < answer[1] - answer[0] + 1:
                answer[0] = i
                answer[1] = j
            j += 1
            if j < len(sequence):
                tmp += sequence[j]
        elif tmp < k:
            j += 1
            if j < len(sequence):
                tmp += sequence[j]
        else:
            tmp -= sequence[i]
            i += 1


    return answer