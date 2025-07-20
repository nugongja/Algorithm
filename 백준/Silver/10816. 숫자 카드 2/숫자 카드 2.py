import sys
input = sys.stdin.readline
from collections import Counter

def solution():
    _ = int(input())
    cards = list(map(int, input().split()))
    card_count = Counter(cards)

    _ = int(input())
    queries = list(map(int, input().split()))

    print(' '.join(str(card_count[q]) if q in card_count else '0' for q in queries))


if __name__ == "__main__":
    solution()