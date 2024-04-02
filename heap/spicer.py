
# Description
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
# 입출력 예
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2
# 입출력 예 설명
# 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

# 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
# 가진 음식의 스코빌 지수 = [13, 9, 10, 12]

# 모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.


# def solution(scoville, K):

#     min_scoville = scoville.pop(1)
#     second_min_scoville = scoville.pop(1)

#     new_scoville = min_scoville + (second_min_scoville *2)


#     return answer


# 0 1 2 3 4 5 7

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


    if len(scoville)==1 and scoville[0]<K:
        return -1
    return c  


heap = [0,1,2,3,4,5,6]
## expected  : 1
#            2  3
#         4  5  6         
#   

heap = [0,3,7,2,4,1,5]

## expected step 1 : 3
#                  7  2
#                4 1 5         
#   
## expected step2  : 3
#                  7  5
#                4 1 2         
# 
## expected step3  : 7
#                  3  5
#                4 1 2         
# 
## expected step4  : 7
#                  4  5
#                3 1 2         
# 
## result = [0,7,4,5,3,1,2]

print(make_min_heap(heap))


heap = [0,5,3,6,2,6,7,9]
print(make_min_heap(heap))
