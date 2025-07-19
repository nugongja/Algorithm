import sys
input = sys.stdin.readline

def solution():

    N, M = map(int, input().split())

    name_to_number = {}
    number_to_name = {}

    for i in range(1, N+1):
        name = input().strip()
        name_to_number[name] = i
        number_to_name[i] = name


    for k in range(M):
        k = input().strip()
        if k.isdigit():
            print(number_to_name[int(k)])
        else:
            print(name_to_number[k])
    




if __name__ == "__main__":
    solution()