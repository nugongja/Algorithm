import sys
input = sys.stdin.readline


def solution(k, tangerine):
    answer = 0
    
    tangerine_dict = {}
    for t in tangerine:
        if t in tangerine_dict:
            tangerine_dict[t] += 1
        else:
            tangerine_dict[t] = 1

    
    sorted_tangerine = sorted(tangerine_dict.values(), reverse=True)


    tmp = 0
    for num_tangerine in sorted_tangerine:
        tmp += num_tangerine
        answer += 1
        if tmp >= k:
            break



    return answer