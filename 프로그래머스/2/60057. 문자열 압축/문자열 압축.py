def solution(s):
    answer = 10001

    for k in range(len(s)//2 + 1, 0, -1):
        length = 0
        tmp = s[:k]
        cnt = 0
        for i in range(0, len(s), k):
            if s[i:min(i+k, len(s))] == tmp:
                cnt += 1
            else:
                if cnt > 1: length += len(str(cnt))
                length += len(tmp)
                tmp = s[i:min(i+k, len(s))]
                cnt = 1

        if cnt > 1: length += len(str(cnt))
        length += len(tmp)

        answer = min(answer, length)

    return answer