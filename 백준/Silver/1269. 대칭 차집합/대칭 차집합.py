import sys
input = sys.stdin.readline

def solution():
    A, B = map(int, input().split())

    list_A = set(map(int, input().split()))
    list_B = set(map(int, input().split()))
    
    print(len(list_A - list_B) +len(list_B-list_A))



if __name__ == "__main__":
    solution()