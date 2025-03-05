def solution(survey, choices):
    answer = ''
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    point = [0, 3, 2, 1, 0, 1, 2, 3]
    for i in range(len(survey)):
        disagree = survey[i][0]
        agree = survey[i][1]
        choice = choices[i]
        if choice >= 5:
            dic[agree] += point[choice]
        elif choice <= 3:
            dic[disagree] += point[choice]
        
    
    answer = ("R" if dic["R"] >= dic["T"] else "T") + ("C" if dic["C"] >= dic["F"] else "F") + ("J" if dic["J"] >= dic["M"] else "M") + ("A" if dic["A"] >= dic["N"] else "N")

    return answer