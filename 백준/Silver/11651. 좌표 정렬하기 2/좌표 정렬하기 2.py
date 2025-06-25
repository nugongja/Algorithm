def solution(n):
    answer = []

    for i in range(n):
        x, y = map(int, input().split())
        answer.append((x,y))

    answer.sort(key=lambda t:(t[1],t[0]))
    

    return answer



if __name__ == "__main__":
    a=int(input())
    answer = solution(a)
    for x, y in answer:
        print(x, y)

