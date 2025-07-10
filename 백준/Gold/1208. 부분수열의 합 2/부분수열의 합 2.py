import sys
from collections import Counter
input = sys.stdin.readline

def get_subset_sums(arr):
    n = len(arr)
    result = []
    for bit in range(1 << n):
        tmp = 0
        for i in range(n):
            if bit & (1 << i):
                tmp += arr[i]
        result.append(tmp)
    return result


def solution():
    answer = 0
    N, S = map(int, input().split())

    A = sorted(list(map(int, input().split())))

    mid = N // 2
    left = A[:mid]
    right = A[mid:]

    left_sum = get_subset_sums(left)
    right_sum = get_subset_sums(right)
    right_counter = Counter(right_sum)

    for val in left_sum:
        answer += right_counter[S - val]

    if S == 0:
        answer -= 1


    print(answer)

if __name__ == "__main__":
    solution()
    
