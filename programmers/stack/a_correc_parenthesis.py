"""
Description
The definition of correctly paired parentheses means that if it is opened with a '(' character, it must be closed with a ')' character.
For instance,

"()()" or "(())()" is a correct parenthesis.
")()(" or "(()(" is an incorrect parenthesis.
Given a string s consisting only of '(' or ')', complete a solution function that returns true if the string s is the correct parenthesis and false if it is not.

Constraints
Length of string s: natural number less than 100,000
The string s consists of only '(' or ')'.
Example
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
Example #1

Same as above example."""


def solution(s):

    count =0 
    for i in range(0,len(s)):
        if  s[i] == '(' :
            count+=1
        elif count > 0 :
            count-=1
        else :
            return False
    
    return count==0


# def solution(s):
#     stack =[]
    
#     for i in range(0,len(s)):    
#         if  s[i] == '(' :
#             stack.append(s[i])
#         elif stack :
#             stack.pop()
#         else : 
#             return False
      
#     return not stack

s1 = "()()"
s2 = "()(())"
s3 = "(()())"
s4 = "((())))())"
s5 = "(()(()))"
s6 ="())()("


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
print(solution(s6))

