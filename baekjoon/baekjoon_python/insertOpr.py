import sys

def solution():
    min_result = float('inf')
    max_result = -float('inf')
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    opr = list(map(int, sys.stdin.readline().strip().split()))

    min_result, max_result = dfs(nums, opr, nums[0], 1, min_result, max_result)

    print(max_result)
    print(min_result)

def dfs(nums, opr, current_result, depth, min_result, max_result):
    if depth == len(nums):

        min_result = min(min_result, current_result)
        max_result = max(max_result, current_result)
        return min_result, max_result
    
    if opr[0] > 0:
        opr[0] -= 1
        min_result, max_result = dfs(nums, opr, current_result + nums[depth], depth + 1, min_result, max_result)
        opr[0] += 1
        
    if opr[1] > 0:
        opr[1] -= 1
        min_result, max_result = dfs(nums, opr, current_result - nums[depth], depth + 1, min_result, max_result)
        opr[1] += 1
        
    if opr[2] > 0:
        opr[2] -= 1
        min_result, max_result = dfs(nums, opr, current_result * nums[depth], depth + 1, min_result, max_result)
        opr[2] += 1
        
    if opr[3] > 0:
        opr[3] -= 1

        if nums[depth] != 0: ## 0으로 나누는 경우 예외처리
            if current_result < 0:
                next_result = -(-current_result // nums[depth]) 
            else:
                next_result = current_result // nums[depth]
            min_result, max_result = dfs(nums, opr, next_result, depth + 1, min_result, max_result)
        opr[3] += 1
    
    return min_result, max_result

solution()
