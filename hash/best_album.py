# Description
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
# 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

# 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.


#같은 키 값이 있을 때는 체이닝 구현 ---> 체이닝을 크기 2인 스택으로 구현. (재생 수가 높은 인덱스 2개만 저장)
# { "classic " : [ {0: 500}, {2: 150}, {3: 800} ] , "pop" : [ {1 : 600}, {4  :2500} ]}


def solution(genres, plays):
    category_array ={}
    category_sum ={}

    for index in range(len(genres)) :
        category = genres[index]
        # 해시 맵 안에 카테고리로 된 키가 있을 때
        if category in category_array and category in category_sum :
            # array 비교
            array = category_array[category]

            array.append(index)
            
            for i in range(len(array)-1) :
                max = i
                for j in range(i+1,len(array)) :
                    if plays[array[max]] < plays[array[j]] : # 같은 경우는 스왑 x 더 작은 인덱스가 살아 남음.
                        max = j 
                array[i], array[max] = array[max], array[i] # swap

            if len(array) > 2 : array.pop()

            category_array[category]= array
            category_sum[category] += plays[index]

        else : 
            category_array[category] = [index]
            category_sum[category] = plays[index]

    sorted_category = sorted(category_sum.items(), key=lambda item: item[1], reverse=True)

    answer = []

    #카테고리 개수
    for key,value in sorted_category :
        answer += category_array[key]

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))  # 출력: [4, 1, 3, 0]