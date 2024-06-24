# Description
# An array arr is given. Each element of arr is a number between 0 through 9. You want to remove all the duplicate numbers in the array arr except for only one. However, the order of each element in the array arr should be maintained. For example,

# When arr = [1, 1, 3, 3, 0, 1, 1], return [1, 3, 0, 1].
# When arr = [4, 4, 4, 3, 3], return [4, 3].
# Write a function solution to return the remaining numbers after removing the duplicate numbers in the array arr except only one.

# Constraints
# Length of array arr : natural number less than or equal to 1,000,000.
# Element of array arr : integer between 0 and 9.
# Examples
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]
# Example #1,2
# It is the same as the example in the problem statement.



#solution 1 - figure out when we consider current num as duplicated and not
# the criteria is number changing moment 
# def solution(arr):
#     answer=[]
#     for i in range(len(arr)):
#         pre = arr[i]
#         print(f'pre ${arr[i]}')
#         if len(arr)-1 == i :
#             answer.append(pre)
#             return answer
#         next = arr[i+1]
#         print(f'next ${arr[i+1]}')
#         if pre !=next :
#              print(f'insert ${pre}')
#              answer.append(pre)
#     return answer



# #solution2 - 

# def solution(arr):
#     answer=[arr[0]]
  
#     for i in range(1, len(arr)):
#         last = answer[-1]
#         if last != arr[i] :
#             print(arr[i])
#             answer.append(arr[i])
#     return answer


# arr= [1,1,3,3,0,1,1]

# arr1 = [4,4,4,3,3]

# print(solution(arr))




