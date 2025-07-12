import sys
import itertools
import re
input = sys.stdin.readline

def to_postfix(tokens, priority):
    output = []
    stack = []

    for token in tokens:
        if token in ['+', '-', '*']:
            while stack and priority[stack[-1]] >= priority[token]: # 스택에 있는게 우선순위 높으면
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)

    while stack:
        output.append(stack.pop())

    return output

def eval_postfix(postfix):
    stack = []

    for token in postfix:
        if token in ['+', '-', '*']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            else:
                stack.append(a * b)
        else:
            stack.append(int(token))

    return stack[0]

def solution(expression):
    
    tokens = re.split(r'([+\-*])', expression)

    operators = [op for op in ['+', '-', '*'] if op in tokens]
  
    max_result = 0
    for ops in itertools.permutations(operators):
        priority = {op: i for i, op in enumerate(ops)}  # 낮은 숫자가 더 높은 우선순위

        postfix = to_postfix(tokens, priority)
        result = eval_postfix(postfix)
        max_result = max(max_result, abs(result))


    
    return max_result