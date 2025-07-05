import sys
input = sys.stdin.readline


moum = ['a', 'e', 'i', 'o', 'u']

def solution():
    L, C = map(int, input().split())
    alp = sorted(list(input().split()))
    answer = []
    
    def dfs(i, J_cnt, M_cnt, tmp):
        nonlocal answer

        tmp.append(alp[i])
    
        
        if len(tmp) == L:
            if M_cnt >= 1 and J_cnt >= 2:
                answer.append(''.join(tmp))
            tmp.pop()
            return
        
        for j in range(i+1, C):
            if alp[j] in moum:
                dfs(j, J_cnt, M_cnt+1, tmp)
            else:
                dfs(j, J_cnt+1, M_cnt, tmp)
    
        tmp.pop()
        
    for i in range(C):
        if moum.count(alp[i]) > 0:
            dfs(i, 0, 1, [])
        else:
            dfs(i, 1, 0, [])


    
    for row in answer:
        print(row)

if __name__ == "__main__":
    solution()
    

    