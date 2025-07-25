import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    unHeard = set(input().strip() for _ in range(N))

    answer = []
    for _ in range(M):
        name = input().strip()
        if name in unHeard:
            answer.append(name)

    answer = sorted(answer)

    print(len(answer))
    for name in answer:
        print(name)
    

if __name__ == "__main__":
    solution()