"""
H-Index
제출 내역
Description
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다."""


# [6,5,3,1,0]
# 6번이상 인용된 책은 1권
# 5번이상 인용된 책은 2권
# 4번이상 인용된 책은 2권
# 3번이상 인용된 책은 3권 ---> return 3
# 2번이상 인용된 책은 3권
# 1번이상 인용된 책은 4권
# 0번이상 인용된 책은 5권

#첫번째 코드 -> 테스트케이스 1개 틀림
def solution(citations) :
    citations.sort(reverse=True) # O(nlogn)
    count = 0
    current = 0
    
    for current in range(citations[0],-1,-1) :
        count=0
        for citation in citations : 
            if current > citation : #현재값보다 인용수가 적을 때
                break 
            count+=1 #현재값만큼 인용된 책의 권수
        if current == count : #h권이 h번 이상 인용되었을 때
            return count
       
# 2번째 코드 -> 테스트케이스
# [11,10,2] 
# 11권 이상 인용된 책 1권
# 10번 이상 인용된 책 2권
# 9번 이상 인용된 책 2권
# 8번 이상 인용된 책 2권
# 7번 이상 인용된 책 2권
# 6번 이상 인용된 책 2권
# 5번 이상 인용된 책 2권
# 4번 이상 인용된 책 2권
# 3번 이상 인용된 책 2권
# 2번 이상 인용된 책 3권 ---> return 2

#위와 같은 경우 2번이상 인용된 책 권수를 구할 때 3권임
# h번 이상 인용한 책이 h권 이상이어야 함, 즉 h==h
# h번 이상 인용된 책이 h+1권일 때 h가 최댓값임.

def solution(citations) :
    citations.sort(reverse=True) # O(nlogn)
    count = 0
    current = 0
    
    for current in range(citations[0],-1,-1) :
        count=0
        for citation in citations :
            if current > citation : #현재값보다 인용수가 적을 때
                break 
            count+=1
        if current == count or current < count: #h권이 h번 이상 인용되었을 때
            return current
 
 
 
 #세번째 코드 [최적화]
 
def solution(citations) :
    citations.sort(reverse=True) # O(nlogn)
    count = 0
    current = 0
    
    for current in range(citations[0],-1,-1) :
        for j in range(count,len(citations)) : #count부터 시작
            if current > citations[j] : #현재값보다 인용수가 적을 때
                break 
            count+=1
        if current == count or current < count: #h권이 h번 이상 인용되었을 때
            return current
