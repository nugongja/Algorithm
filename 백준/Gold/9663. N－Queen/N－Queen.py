import sys
import copy
input = sys.stdin.readline


def solution():
    answer = 0
    N = int(input())
    col = [False]*N
    diag1 = [False]*(2*N-1)  # 좌하->우상 대각선 => i+j == x+y
    diag2 = [False]*(2*N-1)  # 좌상->우하 대각선 => i-j == x-y == i-j+N-1 


    def dfs(r, cnt):
        nonlocal answer
    
        if cnt == N:
            answer += 1
            return

        for c in range(N):
            if not col[c] and not diag1[r-c+N-1] and not diag2[r+c]:
                col[c] = True
                diag1[r-c+N-1] = True
                diag2[r+c] = True
                dfs(r+1, cnt+1)
                col[c] = False
                diag1[r-c+N-1] = False
                diag2[r+c] = False


    dfs(0, 0)


    print(answer)

if __name__ == "__main__":
    solution()
    

    