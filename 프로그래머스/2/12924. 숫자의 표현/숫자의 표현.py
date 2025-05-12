def solution(n):
    answer = 0

    start_idx = 1
    end_idx = 1
    tmp = 1
    while end_idx <= n:
        if tmp < n:
            end_idx += 1
            tmp += end_idx
        elif tmp == n:
            answer += 1
            tmp -= start_idx
            start_idx += 1
        else:
            tmp -= start_idx
            start_idx += 1

    return answer