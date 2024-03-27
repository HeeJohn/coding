import heapq

def scov(a,b):
    return (a+b*2)

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    c=0

    while len(scoville)>=2 and scoville[0]<K:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        x=scov(a,b)
        heapq.heappush(scoville,x)
        c+=1

    if scoville[0]<K:
        return -1

    return c  

