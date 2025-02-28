def solution(ingredient):
    answer = 0
    stack = []

    for c in ingredient:
        stack.append(c)

        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
        
    
    return answer