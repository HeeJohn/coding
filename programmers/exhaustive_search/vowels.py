# Description
# A certain dictionary contains all words that consist only of vowels A, E, I, O, and U that are five-letter long at maximum. The first letter in the dictionary is "A", which is followed by "AA", and so on. The last word will be "UUUUU".

# Suppose that a parameter word is given, where word is a single word. Please write a function solution that returns the rank of that word in the dictionary given above.

# Constraints
# The length of word is between 1 and 5.
# word consists only of the following uppercase letters: A, E, I, O, and U.
# Examples
# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189
# Example #1

# The first word in the dictionary is "A", followed by "AA", "AAA", "AAAA", "AAAAA", "AAAAE", and so on. "AAAAE" is the sixth word in the dictionary, and therefore its rank is 6.

# Example #2

# There will be "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", and "AAAAU", which is followed by "AAAE"--the tenth word in the dictionary, and therefore its rank is 10.

# Example #3

# "I" is the 1563rd word in the dictionary.

# Example #4

# "EIO" is the 1189th word in the dictionary.

# A --->1
# AA  --->2
# AAA ---> 3
# AAAA --->4
# AAAAA --->5


# - 완전 탐색
#     - 자릿수마다 5번씩 카운팅하는 것을 이용
#     - 자릿수가 5번 이고, 자릿수가 모두 채워지기 전에는  자릿수가 먼저 채워져야 함.
#         - ex) A → AA → AAA→ AAAA→ AAAAA →AAAAE
#         - AAAA에서 AAAE가 되려면 먼저 자릿수가 채워지고, 다섯번째 자릿수에서 모음의 모든 카운팅이 끝나야 AAAE가 되고, 다시 AAAEA가 됨.
#     - 각 자릿수에 모음을 변경해가기 전에 다음 자릿수를 카운팅하는 재귀함수를 호출.
#     - 여기서 재귀함수를 탈출하는 경우는 2가지
#         - 찾고자하는 문자열조합이 나왔을 때 → 모든 재귀함수를 빠져나와야 함
#         - 찾고자하는 문자열이 없어서, 카운팅을 마치고, 다시 이전 자릿수로 돌아가는 경우
#         - 따라서 flag를 이용

# - 시간복잡도
#     - 각 자릿수마다 무식하게 모음수만큼 카운팅
#         - 모음의 수 n → 5이므로,
#         - _ _ _ _ _ → 5*5*5*5*5,
#         - 최악의 경우 O(5^n)임.

def tranversal(word, current, depth, flag) :
    vowels= ['A','E','I','O','U']

    for vowel in vowels : 
        flag[1]+=1
        new = current+vowel
        
        if word == new : #탈출 조건[문자 찾았을 때]
            flag[0]= True
            return flag
        
        if depth != 1 : #5자리 밑으로는 더 안들어가기.
            flag = tranversal(word, new, depth-1, flag)
            if flag[0] : return flag
     
    return flag #탈출 조건[현재 루프에서 문자가 없을 때]
    
        
def solution(word) :
    return tranversal(word, '', 5, [False, 0])[1]
    