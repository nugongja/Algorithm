
def binary_search(arr, target):
    # arr은 이미 정렬된 상태
    start = 0 
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid][0] > target:
            end = mid-1
        elif arr[mid][0] == target:
            return mid
        else:
            start = mid+1
    
    return start 

def solution(N):
    answer = []
    A = [0] + list(map(int, input().split())) 
    D = [(0, -1)] # index: 부분순열 길이, value: A의 값
    prev = [0]*(len(A))  # D에 저장될 때 (앞의 값, 나의 A index)를 저장

    A[0] = 0
    for i in range(1, len(A)):
        idx = binary_search(D, A[i])
        if len(D) <= idx:
            D.append((A[i], i))
        if A[i] < D[idx][0]:
            D[idx] = (A[i], i)
        prev[i] = D[idx-1][1]
        


    now = D[-1][1]
    while now != -1:
        answer.append(A[now])
        now = prev[now]

    return answer

if __name__ == "__main__":
    N = int(input())
    answer = solution(N)
    print(len(answer))
    print(' '.join(map(str, reversed(answer))))

    