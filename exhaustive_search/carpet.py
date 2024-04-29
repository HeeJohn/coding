"""Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
"""




# 카펫의 가로 길이 >= 세로길이
# 최소 정사각형 or 가로가 긴 직사각형
# 안에 노랑색을 감싸기 위해서는 안의 사각형보다 가로, 세로로 +2만큼 커야됨.
# 그러면 중요한 것은 안에 노란색 사각형의 모양에 따라 형성되는 브라운의 개수가 맞는가를 판단해야함
# ex) brown : 24, yellow : 24 -> return [8, 6]
# 노랑이 6x4가 아니라 8x3으로 형성되어 있으면 브라운은 10X5의 테두리 길이임.
# (하지만 여기서는 블록이므로, 모서리는 가로, 세로 둘다 포함되는 중복되는 값임)
# (8+2-1)*2 + (3+2-1)*2 
# = 18 + 8  = 26이 됨. 여기서 -1이 세로와 가로가 겹치는 부분
# 이게 24개가 아니기 때문에 아무튼 안됨. 


import math

def qualify(width, height, brown) :
    border =(width +1)*2 + (height+1)*2
    if  border== brown :
        return True
    else : return False


def solution(brown, yellow):
    
    approximate = int(math.floor(yellow**(1/2))) 
    for height in range(approximate,0,-1) :
        if yellow % height == 0 :
            width = yellow//height
            if qualify(width, height, brown) :
                return [width+2, height+2]
            