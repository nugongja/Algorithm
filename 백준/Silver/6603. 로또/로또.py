import sys
input = sys.stdin.readline


def solution():
    lottos = []

    def dfs(i, cnt, k):
        nonlocal tmp, lottos

        if cnt == 6:
            lottos[k].append(" ".join(tmp))
            return
        
        for j in range(i+1, N):
            tmp.append(str(line[j]))
            dfs(j, cnt+1, k)
            tmp.pop()


        return



    k = 0
    while True:
        line = list(map(int, input().split()))
        N = len(line)

        if line[0] == 0: break

        lottos.append([])
        tmp = []
        dfs(0, 0, k)

        k += 1


    for lotto in lottos:
        for case in lotto:
            print(case)
        print()    
    

if __name__ == "__main__":
    solution()
