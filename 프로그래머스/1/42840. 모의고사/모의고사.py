def solution(answers):
    answer = []

    losers = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    n = len(answers)

    max = 0
    for i in range(3):
        tmp = list(answers[j] - losers[i][j%len(losers[i])] for j in range(n)).count(0)
        if tmp > max:
            answer.clear()
            answer.append(i+1)
            max = tmp
        elif tmp > 0 and tmp == max:
            answer.append(i+1)



    return sorted(answer)
    
