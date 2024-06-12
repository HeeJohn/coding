# 하나의 심사대에 동시에 한명만 심사
# 가장 앞에 있는 사람은 2가지 선택지
# 1. 비어있는 곳
# 2. 비어있지는 않지만 더 먼저 끝나는 심사대 선택 (예외가 있을 수 있음)
# !! 구하고자하는 것은 모든 사람이 심사를 받는데 걸리는 시간을 최소화
# 테스트 케이스 : 6명, 심사시간 :  [7, 10]
# 1. 0분 - 4명, 대기시간 : [7, 10] 
# 2. 7분 - 3명, 대기시간 : [7, 3] 
# 3. 10분 - 2명, 대기시간  : [4, 10]
# 4. 14분 - 1명, 대기시간 : [7, 6] 
# 5. 20분 - 1명, 대기시간 : [1, 0] --->  [] 1분 대기 10 > 1 + 7 이 더 작았음.
# 6. 21분 - 0명, 대기시간 : [7, 0]
# 7. 28분 - 종료


def solution(n, times):
    times.sort()
    answer = 0
    min_t=times[0]
    max_t=times[0]*n
    
    while(1):
        count=0
        mid=(min_t+max_t)//2
        for i in times:
            count+=(mid//i)
        if(count>=n):
            max_t=mid
        elif(count<n):
            min_t=mid
        if(min_t==max_t-1):
            answer=max_t
            break


    return answer