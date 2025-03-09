def solution(n, w, num):
    answer = 0

    boxes = [[i for i in range(w*j, w*(j+1))] for j in range(n//w+1)]
    
    for i in range(n//w + 1):
        if i%2 == 1:
            boxes[i].sort(reverse=True)
    
    for i in range(n//w, -1, -1):
        print(boxes[i])
        
    
    target_row = (num-1)//w
    target_col = ((w-1 - (num-1)%w) if target_row%2 == 1 else (num-1)%w)
    print("target_row: ", target_row, "/ target_col: ", target_col)

    for row in range(n//w, target_row, -1):
        if boxes[row][target_col] < n:
            answer += 1

    return answer+1