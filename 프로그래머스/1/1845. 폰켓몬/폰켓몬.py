def solution(nums):
    t = len(nums)//2
    return t if len(set(nums)) > t else len(set(nums))