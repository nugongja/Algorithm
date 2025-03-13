def solution(lottos, win_nums):
    answer = []

    nums = [0]*46

    for k in lottos:
        nums[k] += 1
    
    tmp = 0
    for k in win_nums:      # 맞춘 숫자
        if nums[k] > 0:
            tmp += 1
    
    zero_cnt = lottos.count(0)  # 모르는 숫자

    if zero_cnt == 6:
        h = 1
    else:
        h = 7-(tmp+lottos.count(0)) if tmp > 0 else 6

    l = 7-tmp if tmp > 1 else 6

    return [h, l]