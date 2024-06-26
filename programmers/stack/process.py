
# 프로세스
# 제출 내역
# Description
# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
# 입출력 예
# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# 입출력 예 설명
# 예제 #1

# 문제에 나온 예와 같습니다.

# 예제 #2

# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.


from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    my_doc = [0 for _ in range(len(priorities))] ## 내 문서 위치 알아야해서 만듬
    my_doc[location]=1 # 전체 리스트 중 내문서위치 =1 
    my_doc = deque(my_doc)  
    cnt=0
    while(my_doc): 
        priority = que.popleft() # 문서 pop
        check_my_doc= my_doc.popleft() # 문서 내껀지 유무 pop
        #### 아래 'len(que) >1'은 max함수 사용시 리스트 길이가 2개 이상을 필요로함,이거 없으면 런타임에러뜰수있음. 또, 비교 리스트가 없다는건 마지막에 인쇄했다는 의미.
        if len(que)>1 and  max(que) > priority : # 문서 중요도가 작으면  
            que.append(priority)  # 인쇄 안하고 뒤로 보냄
            my_doc.append(check_my_doc) # 문서 유무도 뒤로 가야징
        else :  ##중요도 베스트여서 인쇄함 
            cnt+=1 # 인쇄 한번 할 때 마다 한개씩 증가
            if check_my_doc == 1 : # 내문서인지 체크 1이면 내꺼임
                answer = cnt # 내문서 뽑은 순서 정답 보내버리고 break
                break
    return answer


# from collections import deque


# def solution(priorities, location):
#     answer = 0
#     data = deque(enumerate(priorities))
#     while data:
#         l, priority = data.popleft()
#         if any(priority < p for _, p in data):
#             data.append((l, priority))
#         else:
#             answer += 1
#             if l == location:
#                 break
#     return answer


## 중요한 포인트는 나의 우선순위보다 큰 프로세스, 같은 프로세스들이다.
# 나보다 큰 프로세스 먼저 제거하고, (카운트)
# 그 다음 프로세스의 인덱스
def solution(priorities, location):
    prior_dict = [(key, value) for key, value in enumerate(priorities)]
    count = 1

    while priorities:
        current = prior_dict.pop(0)
        if current[1] < max(priorities):
            prior_dict.append(current)
        else:
            if current[0] == location:
                return count
            else:
                priorities.pop(current[0])
                count += 1
    return count

 
def hasBiggerDegit(target, priorities) :
    for priority in priorities :
        if target < priority :
            return True
    
    return False


priorities = [2, 1, 3, 2]
location = 2
solution(priorities,location)
priorities =[1, 1, 9, 1, 1, 1]
location = 0
solution(priorities,location)
