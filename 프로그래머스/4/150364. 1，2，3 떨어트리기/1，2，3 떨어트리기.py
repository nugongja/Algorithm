import sys 
import itertools
sys.setrecursionlimit(10**6)

class TreeTraverser:
    def __init__(self, Tree):
        self.Tree = Tree
        self.idxes = [0]*(len(Tree))
        self.n = len(Tree)
    
    def next_leaf(self):
        now = 0
        while self.Tree[now]:
            i = self.idxes[now]
            self.idxes[now] = (self.idxes[now]+1)%len(self.Tree[now])
            now = self.Tree[now][i]
        
        return now


def makeTree(edges, n):
    Tree = [[] for _ in range(n)]

    for p, c in edges:
        Tree[p-1].append(c-1)

    for i in range(0, n):
        Tree[i].sort()

    return Tree

def checkNode(i, cntArr, target, dp):
    return cntArr[i] <= target[i] and cntArr[i] >= dp[target[i]]

def getCombination(count, total):
    for p in itertools.combinations_with_replacement([1,2,3], count):
        if sum(p) == total:
            return list(p)

    return None

# target[i]를 cntArr[i]개의 1,2,3으로 구성한 수열 중,
# 사전순으로 가장 빠른 수열을 하나만 구하면 됨.
def distributeNum(cntArr, target, idx):   
    seq = getCombination(cntArr[idx], target[idx])
    return seq


def solution(edges, target):
    answer = []

    Tree = makeTree(edges, len(target))
    traverser = TreeTraverser(Tree)  

    cntArr = [0]*len(target)
    sequence = []

    dp = [0]*101  # 1,2,3으로 수를 구성했을 때 최소 항 개수
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 101):
         dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + 1


    isPossible = False
    while True:
        now = traverser.next_leaf()
        sequence.append(now)
        cntArr[now] += 1

        if cntArr[now] > target[now]:
            isPossible = False
            break
        
        if checkNode(now, cntArr, target, dp):
            isPossible = all(cntArr[i] >= dp[target[i]] for i in range(len(cntArr)))
            if isPossible:
                break
    
    tmp = []
    if isPossible:
        for i in range(len(cntArr)):
            tmp.append(distributeNum(cntArr, target, i))
    
        for i in range(len(sequence)):
            node = sequence[i]
            answer.append(tmp[node].pop(0))
    else:
        answer = [-1]

    return answer 