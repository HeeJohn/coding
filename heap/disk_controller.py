

import heapq

def process(end_at, tr, job) :
    tr +=(end_at-job[0]+job[1]) # wait time + excution time
    end_at +=job[1] # completion time
    return end_at, tr

def sjf(jobs, end_at, heap) :
    while jobs and jobs[0][0] <= end_at: # 끝난 시간 이전에 요청된 작업 선택
        job = jobs.pop(0)
        heapq.heappush(heap, (job[1], job)) #처리시간을 기준으로 힙 생성
    return heap

def solution(jobs):
    tr= 0 # turning around time
    end_at =0 # completion time
    jobs.sorted(key=lambda x: x[0]) # 요청이 들어온 순서대로 정렬
    heap=[]
    
    while heap or jobs : # 모든 jobs를 처리할 때까지 -> job이 heap 있을 수 있으므로 둘 다 체크
        heap =sjf(jobs,end_at,heap)

        if heap : # 현재 종료시간을 기준으로 그 전에 들어온 요청이 있다는 것
            sj = heapq.heappop(heap) #shortest job
            end_at,tr = process(end_at,tr, sj)
        else : #heap 비면, 먼저 요청이 들어온 job부터 처리
            fr = jobs.pop(0) # first requested job
            end_at,tr = process(end_at,tr, fr)
        
    return tr//len(jobs)
