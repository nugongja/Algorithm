from collections import Counter

def solution(participant, completion):

    dic = {}

    for usr in participant:
        if usr not in dic:
            dic[usr] = 1
        else:
            dic[usr] += 1
    
    for usr in completion:
        dic[usr] -= 1

    
    for key, value in dic.items():
        if value > 0:
            answer = key

    

    return answer