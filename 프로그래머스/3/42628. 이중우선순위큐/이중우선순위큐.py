import heapq
from collections import defaultdict


def solution(operations):
    answer = [0,0]

    max_heap = []
    min_heap = []
    count = defaultdict(int)

    for operation in operations:
        op, value = operation.split(" ")

        if op == 'I':
            heapq.heappush(min_heap, int(value))
            heapq.heappush(max_heap, -int(value))
            count[int(value)] += 1
        elif op == 'D':
            if len(max_heap) == 0:
                continue

            if value == '1':
                while max_heap:
                    tmp = heapq.heappop(max_heap)
                    if count[-tmp] > 0:
                        count[-tmp] -= 1
                        break
            else:
                while min_heap:
                    tmp = heapq.heappop(min_heap)
                    if count[tmp] > 0:
                        count[tmp] -= 1
                        break

        
    while max_heap:
        tmp = heapq.heappop(max_heap)
        if count[-tmp] > 0:
            answer[0] = -tmp
            break
    

    while min_heap:
        tmp = heapq.heappop(min_heap)
        if count[tmp] > 0:
            answer[1] = tmp
            break
    


    return answer