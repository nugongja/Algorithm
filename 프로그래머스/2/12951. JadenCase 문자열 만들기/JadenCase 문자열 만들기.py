def solution(s):
    answer = ""

    isUpper = True
    for i in range(len(s)):
        if isUpper and s[i] != ' ':
            isUpper = False
            answer += s[i].upper()
        elif s[i] != ' ':
            answer += s[i].lower()
        else:
            answer += ' '
            isUpper = True

    return answer