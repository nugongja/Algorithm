import heapq

def solution(k, score):
    answer = []

    pq = []
    for s in score:
        if len(pq) < k:
            heapq.heappush(pq, s)
        else:
            heapq.heappushpop(pq, s)

        answer.append(pq[0])

    return answer