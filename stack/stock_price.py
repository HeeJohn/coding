# Description
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.


def solution(prices):
    stack= [0] 
    answer = [0] * len(prices)
    counter =1
    for i in range(1, len(prices)) :
            if prices[stack[-1]] <= prices[i] :
                 stack.append(i)
                 counter =1
            else :
                while stack and  prices[stack[-1]]  > prices[i] :
                    answer [stack.pop()] = counter
                    counter+=1
                stack.append(i)    

    while stack :
         index = stack.pop()
         answer[index ] = len(prices) - index -1

    return answer

# def solution(prices):

#     times = [0] * len(prices)
#     stack = []
#     for i in range(len(prices)):
#         for s,idx in stack:
#             times[idx] += 1
#         while stack and stack[-1][0] > prices[i]:
#             stack.pop()
#         stack.append((prices[i], i))

#     return times


prices=[1, 2, 3, 2, 3]
expected = [4,3,1,2,1]

prices3 = [3, 2, 4, 1, 1]
# [1, 2, 1, 1, 0]
prices1=[1,2,2,1,3,1,2]
expected1 = [7,2,1,4,]
print(prices3)
print(solution(prices3))
# print(prices1)
# print(solution(prices1))