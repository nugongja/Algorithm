import sys
from math import inf
input = sys.stdin.readline


def solution():
    answer = [-inf, inf]
    N = int(input())
    arr = list(map(int, input().split()))
    ops = list(map(int, input().split()))


    def dfs(idx, tmp):
        nonlocal answer
        # 종료 조건
        if idx == N:
            answer[0] = max(answer[0], tmp)
            answer[1] = min(answer[1], tmp)
            return

        # 반복문
        for i in range(4):
            if ops[i] > 0:
                ops[i] -= 1
                if i == 0:
                    dfs(idx+1, tmp+arr[idx]) 
                elif i == 1:
                    dfs(idx+1, tmp-arr[idx])
                elif i == 2:
                    dfs(idx+1, tmp*arr[idx])
                else:
                    if tmp*arr[idx] < 0:
                        dfs(idx+1, -(abs(tmp)//abs(arr[idx]))) 
                    else:
                        dfs(idx+1, tmp//arr[idx]) 
                ops[i] += 1  

    dfs(1, arr[0])

    print(answer[0])
    print(answer[1])

if __name__ == "__main__":
    solution()
    

    