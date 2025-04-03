import sys
def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_value = sys.maxsize
    idx = -1

    for i, value in enumerate(arr):
        if value < min_value:
            min_value = value
            idx = i
    
    arr.remove(min_value)     
        
    return arr