import sys
input = sys.stdin.readline




def solution(n):
    answer = []

    # n-1개를 tmp로 옮기고, n을 C로 옮긴다.
    # target: 원판 n
    # A: 현재 n개의 원판들이 있는 기둥 
    # B: 보조 기둥 (n-1개 원판들이 옮겨질)
    # C: n을 옮기고자 하는 타깃 기둥
    def hanoi(target, A, B, C):
        nonlocal answer

        if target == 0:
            return

        hanoi(target-1, A, C, B)
        answer.append([A, C])
        hanoi(target-1, B, A, C)


        return


    hanoi(n, 1,2,3)

    return answer
