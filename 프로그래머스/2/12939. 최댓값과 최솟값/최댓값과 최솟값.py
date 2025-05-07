def solution(s):
    answer = ''

    li = list(map(int, s.split(' ')))
    li = sorted(li)


    answer = str(li[0]) + " " + str(li[-1])

    return answer