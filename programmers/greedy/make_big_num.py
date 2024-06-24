"""Description
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"""
## 첫번째 코드 테스트 케이스 하나 틀림.

# def solution(number, k):
#     stack = []
#     i = 0
#     ln = len(number)
    
#     # k개 모두 제거할 때까지 반복
#     while k > 0:
#         #마지막 숫자가 현재 숫자보다 작으면 스택에서 제거
#         if stack and stack[-1] < number[i]:
#             stack.pop()
#             k -= 1
#             continue
#         stack.append(number[i])
#         i += 1
        
#         #모든 문자 순회했으면 종료
#         if i >= ln:
#             return ''.join(stack)
    
#     return ''.join(stack) + number[i:]
    
    
    
## 두번째 코드
def solution(number, k):
    stack = []
    i = 0
    ln = len(number)
    
    # k개 모두 제거할 때까지 반복
    while k > 0:
        #마지막 숫자가 현재 숫자보다 작으면 스택에서 제거
        if stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
            continue
        stack.append(number[i])
        i += 1
        
        if i >= ln:
		        ## 모든 숫자를 순환했는데, k가 0이 아닐 수 있음
		        # ex) 9876의 경우 2만큼 빼야 한다면, 뺄게 없음 
		        # 그냥 뒤에서 부터 뺌
            return ''.join(stack[0:-k]) ##수정된 부분 
	    
    return ''.join(stack) + number[i:]    



"""

### 알고리즘

- 그리디 + 스택

### 시간복잡도

- n은 문자열의 길이
- k은 빼는 횟수
- while문은 최선의 경우 k번 반복, 최악의 경우 n+k-1만큼 반복
    - O(n)
- 문자열 이어붙히기
    - stack 길이 → m
    - O(m) or O(m+n-i)
        - 결론 O(n)
- 전체 시간 복잡도
    - O(n)

### 설명

- 숫자 문자열의 앞에서부터 순환하면서 숫자를 스택에 넣고,
- 들어오는 값보다 스택 내부 더 작은 값은 빼버림.

***2가지 경우 수로 답을 구함.***

- k만큼 문자열에서 제거한 경우
    - 문자열을 다 순환하기도 전에 숫자를 뺏기 때문에 stack에는 일부 안 담길 수 있음
    - 이를 i부터 이어붙여주기
- 모든 숫자를 순환한 경우
    - 모든 숫자를 스택에 넣었는데, k가 0이 아닐 수 있음
        - ex) 9876의 경우 2만큼 빼야 한다면, 뺄게 없음
    - 그냥 뒤에서 부터 뺌
""" 