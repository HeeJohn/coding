from collections import deque

def isNotWall(x, y, w, h, visited, maps):
    #범위를 벗어나지 않고, 방문한 적이 없고, 벽이 아닌 블록
    return (0 <= x < w and 0 <= y < h) and  (maps[y][x] == 1 and not visited[y][x])

def solution(maps):
    h = len(maps)
    w = len(maps[0])

    visited = [[False] * w for _ in range(h)]
    queue = deque([(0, 0, 1)])  #x, y, spaces
    
    while queue:
        x, y, spaces = queue.popleft()
        visited[y][x] = True
        
        #도착
        if x == w-1 and y == h-1:
            return spaces
        
        #가장 빠르게 움직이려면, 좌상단에서 우하단으로 움직여야 함 (하,우로 이동이 우선순위)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]: #하, 우, 좌, 상 순
            newX, newY = x + dx, y + dy
            #움직일 수 없는 영역 벽으로 간주.
            if isNotWall(newX, newY, w, h, visited, maps):
                queue.append((newX, newY, spaces + 1))
                visited[newY][newX] = True
    return -1



"""
- **알고리즘**
    - **너비 우선 탐색**
        - 탐색할 때 주변을 우선적으로 탐색하고, 가능한 인접 블록부터 이동하며 최단 거리를 찾음.
        - 이때 인접 블록에 대한 탐색 순서에 우선 순위를 둬서 [하, 우, 좌, 상]으로 이동하고, 목적지에 도달했을 때 바로 종료시킴.
        
- **시간 복잡도**
    - 이동한 위치에서 인접한 (하, 우, 좌, 상)블록을 확인함.
        - 이동한 블록에 대하여 인접한 동서남북 4방향 확인 O(4)
    - 최악의 경우 deque에 가능한 모든방향을 계속 넣을 수 있음.
        - 주어진 맵의 크기가 h x w이라면, 모든 블록으로 한번 씩 이동하게 될 수도 있음
        - 결론적으로 시간 복잡도는 O(nm)이 됨.
- **설명**
    - 이미 지나온 곳까지는 블록(spaces)가 카운트를 했기 때문에 뒤로 돌아갈 필요 x
    - 범위에서 벗어나거나, 블록의 값이 0이거나, 방문한 곳은 벽으로 간주
    - 벽이 아닌 위치로 이동하면서, 이동한 위치에서 파생되는 이동 경로를 탐색 후 이동을 반복"""