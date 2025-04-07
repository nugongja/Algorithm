def solution(s):
    answer = ''

    isEven = True
    for i in range(len(s)):
        if s[i] == ' ':
            isEven = False

        if isEven:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        
        isEven = not isEven
        
        


    return answer
