import sys
input = sys.stdin.readline


def solution(triangle):
    answer = 0

    depth = len(triangle)-1

    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]

    dp[depth] = triangle[depth]
    
    for i in range(depth-1, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

    answer = dp[0][0]

    return answer