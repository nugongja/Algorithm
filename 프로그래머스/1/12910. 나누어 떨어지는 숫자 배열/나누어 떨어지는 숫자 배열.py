def solution(arr, divisor):
    return sorted([word for word in arr if word%divisor == 0]) if len([word for word in arr if word%divisor == 0]) > 0 else [-1]
