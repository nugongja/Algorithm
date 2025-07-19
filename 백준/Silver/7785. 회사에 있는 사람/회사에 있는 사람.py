import sys
input = sys.stdin.readline



def solution():
    answer = 0

    N = int(input())
    dic = {}

    for _ in range(N):
        name, status = map(str, input().split())
        if status == 'leave':
            dic.pop(name)
        else:
            dic[name] = 1
    
    dic = dict(sorted(dic.items(), reverse=True))

    for key, _ in dic.items():
        print(key)
    
    return answer
    
if __name__ == "__main__":
    solution()