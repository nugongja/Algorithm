def solution(board, moves):
    answer = 0
    n = len(board)

    stack = []

    height = [-1]*n
    for col in range(n):
        for row in range(n):
            if board[row][col] != 0:
                height[col] = row
                break
            

    for col in moves:
        if height[col-1] == n:
            continue

        tmp = board[height[col-1]][col-1]
        height[col-1] += 1

        if len(stack) > 0 and stack[-1] == tmp:
            stack.pop()
            answer += 1
        else:
            stack.append(tmp)
        

    return answer*2