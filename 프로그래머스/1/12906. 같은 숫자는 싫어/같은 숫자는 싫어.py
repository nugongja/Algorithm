def solution(arr):
    arr = [-1] + arr
    return [arr[i] for i in range(1, len(arr)) if arr[i] != arr[i-1]]
