def solution(numbers, hand):
    answer = ''
    
    numbers = list(map(str, numbers))


    idx_left = (3,0)
    idx_right = (3,2)

    keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    

    for number in numbers:
        row = (int(number)-1)//3
        col = (int(number)-1)%3

        if number == '0':
            row = 3
            col = 1

        if col == 0:
            answer += 'L'
            idx_left = (row, col)
        elif col == 2:
            answer += 'R'
            idx_right = (row, col)
        else:
            if (abs(row-idx_right[0]) + abs(col-idx_right[1])) < (abs(row-idx_left[0]) + abs(col-idx_left[1])):  # 오른손이 더 가까울 때 -> 상하좌우로만 움직임 -> 점과 점의 거리 계산 못 함
                answer += 'R'
                idx_right = (row, col)
            elif (abs(row-idx_right[0]) + abs(col-idx_right[1])) > (abs(row-idx_left[0]) + abs(col-idx_left[1])): # 왼손이 더 가까울 때
                answer += 'L'
                idx_left = (row, col)
            else:
                if hand == "right":
                    answer += 'R'
                    idx_right = (row, col)
                else:
                    answer += 'L'
                    idx_left = (row, col)

    return answer
