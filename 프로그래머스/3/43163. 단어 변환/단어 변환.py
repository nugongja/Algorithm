import sys
input = sys.stdin.readline
from collections import deque

def compare(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt > 1: return 0
    
    return 1



def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)

    answer = 0
    dic = {}

    # 트리 만들기 (연결관계 설정)
    for word1 in words:
        dic[word1] = []
        for word2 in words:
            if compare(word1, word2):
                dic[word1].append(word2)
                

    # begin에서 target으로의 최단거리 구하기 -> BFS
    queue = deque()
    queue.append((begin, 0))  # node, cost

    
    while queue:
        curr_node, curr_cost = queue.popleft()
        if curr_node == target:
            answer = curr_cost
            break

        for next_node in dic[curr_node]:
            queue.append((next_node, curr_cost+1))

    return answer
    

if __name__ == "__main__":
    begin, target, words = "hit"	,"cog",	["hot", "dot", "dog", "lot", "log"]
    answer = solution(begin, target, words)
    print(answer)