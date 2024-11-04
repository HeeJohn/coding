

import heapq

def process(end_at, tr, job) :
    tr += (end_at - job[0] + job[1]) # 대기 시간 + 실행 시간
    end_at += job[1] # 완료 시간
    return end_at, tr

def sjf(jobs, end_at, heap) :
    while jobs and jobs[0][0] <= end_at: # 끝난 시간 이전에 요청된 작업 선택
        job = jobs.pop(0)
        heapq.heappush(heap, (job[1], job)) # 처리 시간을 기준으로 힙 생성
    return heap

def solution(jobs):
    tr = 0 # 턴어라운드 시간
    end_at = 0 # 완료 시간
    jobs.sort(key=lambda x: x[0]) # 요청이 들어온 순서대로 정렬
    heap = []
    total_tasks = len(jobs)

    while heap or jobs : # 모든 작업를 처리할 때까지
        heap = sjf(jobs, end_at, heap)

        if heap : # 현재 종료 시간을 기준으로 그 전에 들어온 요청이 있다는 것
            sj = heapq.heappop(heap) # 가장 짧은 작업
            end_at, tr = process(end_at, tr, sj[1])
        else : # heap이 비면, 먼저 요청이 들어온 작업부터 처리
            fr = jobs.pop(0) # 첫 번째 요청된 작업
            end_at, tr = process(end_at, tr, fr)

    return tr // total_tasks




jobs = [[1, 4], [7, 9], [1000, 3]]
# return = 5
print(solution(jobs))

jobs = [[7, 8], [3, 5], [9, 6]]
# return = 9
print(solution(jobs))

jobs = [[0, 3], [10, 1]]
# return 2
print(solution(jobs))

jobs = [[0, 3], [4, 4], [5, 3], [7, 1]]
# return 4
print(solution(jobs))
