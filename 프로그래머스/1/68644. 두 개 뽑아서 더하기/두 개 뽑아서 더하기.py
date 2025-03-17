import itertools

def solution(numbers):

    dic = {}

    iterator = itertools.combinations(numbers, 2)
    for arr in iterator:
        tmp = arr[0]+arr[1]
        if tmp not in dic:
            dic[tmp] = 1
    

    return sorted([k for k in dic])