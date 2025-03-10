import itertools

def solution(n, q, ans):
    answer = 0

    iterator = itertools.combinations(range(1, n+1),5)
    for arr in iterator:
        arr = list(arr)  # 튜플을 리스트로 변환
        isPossiboe = True
        for i in range(len(q)):
            tmp = sum(1 for x in arr if x in q[i])
            if tmp != ans[i]:
                isPossiboe = False
                break


        if isPossiboe:
            answer += 1


    return answer
    

