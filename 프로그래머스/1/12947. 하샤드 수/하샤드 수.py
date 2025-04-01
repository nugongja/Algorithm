def solution(x):

    tmp = sum([int(digit) for digit in str(x)])
    

    return True if x%tmp == 0 else False