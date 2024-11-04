from collections import deque
def bfs(board, start_y, start_x, end_y, end_x):
    queue = deque([(start_y, start_x, 0)])
    board[start_y][start_x] = -1 

    while queue:
        y, x, distance = queue.popleft()
        
        if (y, x) == (end_y, end_x): ## 도착
            return distance // 2  

        for dy, dx in  [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if board[ny][nx] == 1:
                board[ny][nx] = -1 # 지나온 곳 벽으로 만들기
                queue.append((ny, nx, distance + 1))
                
def makeBoard(rectangle):
    board = [[0] * 102 for _ in range(102)]  #선을 면으로 만들기 위함.
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2  # 마찬가지로, 점의 연속은 선인데, 그것을 면적으로 만들기 위해 
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if y1 < y < y2 and x1 < x < x2:  #y1, y2, x1, x2는 포함 안됨.
                    board[y][x] = -1
                elif board[y][x] != -1:  #포함 안되는 부분 다른 사각형에 의해 overlap 안되면, 외부 경계선이 됨.
                    board[y][x] = 1
    
    return board

def solution(rectangle, character_x, character_y, item_x, item_y):
    return bfs(makeBoard(rectangle), character_y * 2, character_x * 2, item_y * 2, item_x * 2)
