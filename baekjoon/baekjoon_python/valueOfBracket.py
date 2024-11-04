import sys

def solution():
    input_str = sys.stdin.readline().strip()
    stack = []
    is_valid = True
    value = 0
    temp = 1

    for i in range(len(input_str)):
        char = input_str[i]
        if char == '(':
            stack.append(char)
            temp *= 2
        elif char == '[':
            stack.append(char)
            temp *= 3
        elif char == ')':
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            if input_str[i - 1] == '(':
                value += temp
            stack.pop()
            temp //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                is_valid = False
                break
            if input_str[i - 1] == '[':
                value += temp
            stack.pop()
            temp //= 3
    
    if stack:
        is_valid = False

    if is_valid:
        print(value)
    else:
        print(0)

solution()
