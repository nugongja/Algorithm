import sys
input = sys.stdin.readline




def solution():
    answer = 0
    dic = {}

    N, M = map(int, input().split())

    for _ in range(N):
        dic[input().strip()] = 1
    
    for _ in range(M):
        tmp = input().strip()
        if tmp in dic:
            answer += 1
    

    print(answer)

if __name__ == "__main__":
    solution()
    

    