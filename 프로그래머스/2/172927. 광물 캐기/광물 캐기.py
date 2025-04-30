import math
from queue import PriorityQueue

def solution(picks, minerals):
    answer = 0
    
    dic = {"diamond":0, "iron":1, "stone":2}
    piro = [[1,1,1], [5,1,1], [25,5,1]]

    minerals = minerals[:min(5*sum(picks), len(minerals))]

    for i in range(len(minerals)):
        minerals[i] = dic[minerals[i]]
    
    idx = [[0,0,0] for _ in range(int(math.ceil(len(minerals)/5)))]
    cnt = len(idx)

    for i in range(len(idx)):
        idx[i][0] = sum(list(piro[0][minerals[j]] for j in range(i*5, min(i*5+5, len(minerals)))))
        idx[i][1] = sum(list(piro[1][minerals[j]] for j in range(i*5, min(i*5+5, len(minerals)))))
        idx[i][2] = sum(list(piro[2][minerals[j]] for j in range(i*5, min(i*5+5, len(minerals)))))
    

    pq = PriorityQueue()
    for i in range(3):
        if pq.qsize() == cnt:
            break
        for j in range(picks[i]):
            pq.put(-i)
            if pq.qsize() == cnt:
                break
 
    print(idx)

    while cnt > 0:
        gock = -pq.get()
        print(gock)

        min_value = 200
        min_idx = -1
        for i in range(len(idx)):
            if min_value > idx[i][gock]:
                min_value = idx[i][gock]
                min_idx = i
        print("idx: ", i, "value: ", min_value)
        answer += min_value
        idx[min_idx][0] = 200
        idx[min_idx][1] = 200
        idx[min_idx][2] = 200

        cnt -= 1



    return answer