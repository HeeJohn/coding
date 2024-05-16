### 첫번째 코드 # 합격률 35퍼

# 블록은 회전 가능, 뒤집기는 불가 -> 방향성이 중요 (모양이 같아야 함)
# 빈 공간이 남으면 안됨 -> 딱 맞는 것만 끼울 수 있음 (개수가 같아야 함)
# 블록은 최대 1개에서 최대 6개
# 한개나 두개까지는 뒤집는 것과 돌리는게 사실 상 동일 (개수만 같으면 해결됨)
# 3부터 6개짜리를 고려하면 됨.
# 일단 개수가 같으면 비교는 해볼 수 있음 근데, 방향성과 모양을 어떻게 판단해야 될까??
# 1. bfs로 보드와 블록에서 좌표(모형) 추출 
# 2. 먼저 블록과 빈칸의 크기로 후보군을 만듬
# 3. 블록과 빈칸의 크기가 같으면 회전시켜가면서 비교
# 4. 비교하기 쉽도록 상대좌표로 변환 계산 
# 5. 회전시키다가 일치하면 블록을 제거와 동시에 길이만큼 채움으로 계산

from collections import deque

def move_if_can(src, m, t, queue, visited) :
    ty, tx = src[1], src[0]
    for y, x in [(1,0), (-1,0), (0,1),(0,-1)] : # 방향
            newy, newx = ty+y, tx+x
            if not 0 <= newx < len(m[0]) or not 0 <= newy < len(m) :
                continue
            if not visited[newy][newx] and m[newy][newx] == t :
                visited[newy][newx] = True
                queue.append((newx, newy))
    return queue, visited

def find_block(m, t) : #map, target
    block_set = []
    h = len(m)
    w = len(m[0])
    visited = [[False] *(w) for _ in range(h)]
    
    for y in range(h) :
        for x in range(w) :
            if not visited[y][x] and m[y][x] == t :
                b = []
                visited[y][x] = True
                queue = deque([(x,y)])
                while queue :
                    src = queue.popleft()
                    b.append(src)
                    queue, visited = move_if_can(src, m, t, queue, visited)
                block_set.append(b)
    return block_set
    
def fill_under3(g_b, t_b) :
    used_b = 0
    g_b.sort(key=lambda x : len(x), reverse=True)
    t_b.sort(key=lambda x : len(x), reverse=True)
    
    while len(g_b[-1]) < 3 :
        g = g_b.pop()
        if len(g) == len(t_b[-1]) :
            t_b.pop()
            used_b += len(g)
    
    while len(t_b[-1]) < 3 : #해결 못하는 블록 버리기
        t_b.pop()
    
    return g_b, t_b, used_b

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            ret[x][N-1-y] = m[y][x] 
    return ret

def is_match(board, block):
    # 애초에 감싸는 직사각형 길이가 다르면 다른 도형임
    if len(board) != len(block) : 
        return False
    
    for bd, bk in zip(board, block) :
        for i, j in zip(bd, bk) :
            if i !=j : return False
    
    return True           

def adjust_point(b) :

    min_x = min(p[0] for p in b)
    min_y = min(p[1] for p in b)
    max_x = max(p[0] for p in b)
    max_y = max(p[1] for p in b)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    bigger = max(height, width)
    
    square = [[0] * bigger for _ in range(bigger)]
    
    for p in b:
        adj_x = p[0] - min_x
        adj_y = p[1] - min_y
        square[adj_y][adj_x] = 1
    
    return square

def fill_if_fit(board, blocks, used_b) :
    candidates = []
    
    while board and blocks : # 둘 중 하나 빌 때까지
        frag = board.pop()

        ## 이미 후보군이 있으면, 후보군의 블록 길이가 같은지 확인
        if candidates and len(frag) != len(candidates[0]) :
            candidates = []
        
        ## 비어있으면 블록 개수가 같은 후보군 확보
        if not candidates : 
            while blocks and len(blocks[-1]) == len(frag) :
                candidates.append(blocks.pop())
            
        print(frag)
        print()
        print(candidates)
        print()
        is_matched = False
        adj_spot = adjust_point(frag) 
        
        for candidate in candidates :
            adj_cand = adjust_point(candidate)
            
            if is_match(adj_spot, adj_cand) : #회전 전
                is_matched = True
            else : 
                for _ in range(3) : #회전
                    rotated_bk = rotate_90(adj_cand)
                    if is_match(adj_spot, rotated_bk) : 
                        is_matched = True
                        break
                    adj_cand = rotated_bk
                
            if is_matched :
                candidates.remove(candidate) # 채운 블록은 제거
                used_b+=len(candidate)
                break
                    
    return used_b


def solution(game_board, table):
    g_b = find_block(game_board, 0)
    t_b = find_block(table, 1)
    g_b, t_b, used_b = fill_under3(g_b, t_b)
    
    return fill_if_fit(g_b, t_b, used_b)