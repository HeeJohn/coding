# N -> 이용숫자
# number -> 목표
# 최솟값이 8보다 크면 -1을 return

# 계산 할 수 있는 최소 연산의 종류 
# 1. (5 / 5) - 나누기는 1을 만들 수 있음.
# 2. (5 + 5) - 더하기는  N*2
# 3. (5 - 5 ) - 빼기는 0 
# 4. (5 * 5) - 곱하기는 N^2
# 5. 55 - 문자열 이어붙히기 n*11

# bottom-up 방식으로 접근해야 될거 같음..
# 쪼갤 수 있는 데까지 쪼개야 할듯.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 11을 2로 나눈기
# 11 = 2+2+2+2+2 -> 나머지 1

# 11 = 2 + 2 + 2 + 2 + 2 + (2/2)
# 11 = (2+2) + (2+2) + 2 + (2/2)
# 11 = 2*2 + 2*2 + 2 + (2/2)
# 11 = 2*(2+2) + 2 + (2/2) 3


###
### 모르겠음. GPT한테 위의 접근법만 제시하고, bottom-up 방식으로 짜달라고 함.
### 내일 다시 풀어봐야지... 뽈뽈뽈



def solution(N, number):
    # 가능한 최댓값으로 초기화
    answer = 9
    
    # 연산 결과를 저장하는 집합들의 리스트
    # 각 집합은 연산 횟수에 따라 결과를 저장함
    dp = [set() for _ in range(9)]
    
    # 각 집합에 초기값 N을 추가
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))


    # 연산 횟수를 증가시키며 모든 경우를 탐색
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        # 목표 숫자가 현재 집합에 포함되어 있다면 최솟값 갱신
        if number in dp[i]:
            answer = min(answer, i)
            # 최솟값이 제한사항을 넘어가면 -1 반환
            if  answer <= 8 : return -1
            return answer

# 예제 테스트
print(solution(5, 12)) # 4
print(solution(2, 11)) # 3
