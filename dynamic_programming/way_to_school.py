"""Description
계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.
가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

제한사항
격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
물에 잠긴 지역은 0개 이상 10개 이하입니다.
집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
입출력 예
m	n	puddles	return
4	3	[[2, 2]]	4
"""


# 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return
# 맵 크기는 (m+1)*(n+1) 테두리는 infite로 채워야 함.
# 움직일때마다 움직임을 카운트해야 됨.
# 집은 [1][1] 이고 도착지는 [m][n]임
# 최단 루트는 항상 오른쪽으로, 아래로 가야됨. 
# 왼쪽으로 가거나, 위로 가면 최단거리가 나올 수 없음
# 최단거리로 도착하면 add하고, 
# top to bottom 식으로 구현



def makeMap(m,n, puddles) :
    mp = []
    
    for h in range(n+2) :
        if h == 0 or h == n+1 : #테두리
            mp.append([-1]*(m+2))
            continue
        mp.append([])
        for w in range(m+2) :
            if w == 0 or w== m+1 :  #테두리
                mp[h].append(-1)
            else :
                mp[h].append(0)
    
    # 웅덩이 배치
    for puddle in puddles :
        mp[puddle[1]][puddle[0]] = -1
    
    return mp


def moveIfPossible (posX, posY, routes, mp, m, n) :
    # 탈출조건 1  : 도착하면 그 루트를 카운트 
    if posX == m and posY == n : 
        return routes+1
    # 좌로 이동
    if posX < m+1 and mp[posY][posX+1] != -1 :
        routes = moveIfPossible(posX+1, posY, routes, mp, m, n) 
    # 하로 이동
    if posY < n+1 and mp[posY+1][posX] != -1 :
        routes = moveIfPossible(posX, posY+1, routes, mp, m, n) 
    # 탈출조건 2  : 갈 곳이 없을 때
    return routes 

def solution(m, n, puddles):
	    return  moveIfPossible(1, 1, 0, makeMap(m,n,puddles), m, n)% 1000000007 