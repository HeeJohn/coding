"""
Description
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
입출력 예
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3"""




# 구명보트는 최대 2명 and 무게 제한 있음.

def canOnBoard(limit, boat, person) :
    
    if boat+person > limit : 
        return False
    return True

def solution(people, limit):
    people.sort(reverse=True)
    light = len(people)-1
    count = 0
    
    for i in range(len(people)) : 
        count +=1
        if canOnBoard(limit, people[i], people[light]) :
            light -=1
        
            
        if i >= light : return count  


"""        ### 알고리즘

- 그리디

### 시간복잡도

- n은 len(people) ⇒ 사람수
- people.sort(reverse=True)
    - 몸무게 많이 나가는 순서부터 가벼운 순서까지 정렬
    - O(nlogn)
- for i in range(len(people)) :
    - 무거운 사람부터 순회
        - 가장 무거운 사람과 가장 가벼운 사람의 조합이 limit을 안 넘으면 2명 태울 수 있음
        - 따라서, 순회하는 횟수 count +=1와 같음 ⇒ 최소 보트 수 만큼
        - O(count) 만큼 n≥count임
- 전체 시간 복잡도
    - remove 연산 ⇒ O(n)
- 전체
    - O(nlogn)

### 설명

- 가장 무거운 사람과 + 가장 가벼운 사람의 조합이 limit를 안 넘으면, 보트를 절약할 수 있음
- for문에서 차례대로 무거운 사람을 태우는데 (count+=1), 여기서 가벼운 사람을 태울 수 있는지 확인하고, 태울 수 있으면 light-=1하여 나중에 for문이 마지막 사람까지 개개인을 태우기 전에 종료되게 함. → 이미 보트에 태운 사람으로 간주하여 태울 필요 없음
- if i >= light : return count
    - 그 인덱스가 서로 교차하면 모든 사람을 다 태운 것임. 따라서, count를 반환함"""