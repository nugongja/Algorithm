import sys
from collections import defaultdict, Counter
input = sys.stdin.readline


def solution():
    answer = 0
    N, S = map(int, input().split())

    A = list(map(int, input().split()))
    dic = defaultdict(int)

    def get_subset_sums(start, end, isLeft):
        nonlocal answer, dic
        sums = []

        for i in range(start, end):
            for j in range(len(sums)):
                sums.append(A[i]+sums[j])
            sums.append(A[i])

  
        for v in sums:
            if v == S:
                answer += 1  # 단독으로 S 만족하는 경우

            if isLeft:
                dic[v] += 1
            else:
                answer += dic[S-v]

    get_subset_sums(0, N//2, True)
    get_subset_sums(N//2, N, False)

        
    print(answer)

if __name__ == "__main__":
    solution()
    
