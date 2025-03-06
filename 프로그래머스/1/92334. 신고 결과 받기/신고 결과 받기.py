def solution(id_list, report, k):
    n = len(id_list)
    answer = [0]*n

    
    count = [[] for _ in range(n)]
    for line in report:
        victim, crimial = line.split(" ")
        if id_list.index(victim) not in count[id_list.index(crimial)]:
            count[id_list.index(crimial)].append(id_list.index(victim))
    
    for crimial in count:
        if len(crimial) >= k:
            for victim in crimial:
                answer[victim] += 1



    return answer