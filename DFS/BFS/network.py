

# ## 첫번째 코드 #복습 겸 union -find 이용


# class Tree:
#     def __init__(self, n):
#         self.parent = list(range(n)) 
#         self.depth = [0] * n
    
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x] 
		
#     def union(self, rootV1, rootV2):
#         if self.depth[rootV1] < self.depth[rootV2]:
#             self.parent[rootV1] = rootV2 
#         elif self.depth[rootV1] > self.depth[rootV2]:
#             self.parent[rootV2] = rootV1
#         else: 
#             self.parent[rootV1] = rootV2 
#             self.depth[rootV1] += 1

# def isConnected(computer) :
#     if computer == 1 :
#         return True
#     return False

# def countSubTree(n, tree):
#     roots = set()
#     for i in range(n):
#         roots.add(tree.find(i))
#     return len(roots)


# def solution(n, computers):
#     tree = Tree(n)

#     for i in range(n): 
#         for j in range(n) :        
#             #자기 자신은 제외, 당연히 1
#             if i == j : 
#                 continue 
#             if isConnected(computers[i][j]) : 
#                 rootV1 = tree.find(i) 
#                 rootV2 = tree.find(j) 
#                 print(rootV1, rootV2)
#                 #spanning tree를 만족하는지 확인 
#                 if rootV1 != rootV2: 
#                     #현재 노드들의 집합(서브트리) 합치기
#                     tree.union(rootV1, rootV2) 
                
#     return countSubTree(n, tree)
    
    
	    ## 두번째 코드 # 인접리스트로 구현
	   
class Graph:
    def __init__(self, n):
        self.adjList = [[] for _ in range(n)] #인접리스트로 그래프 구현
        self.visited = [False] * n

    def addEdge(self, u, v):
        #연결된 정점에 대한 인덱스값을 가짐
        self.adjList[u].append(v) 
        self.adjList[v].append(u)

    def dfs(self, vtx):
        self.visited[vtx] = True 
        for p in self.adjList[vtx]: # vertex와 연결된 인접 정점들
            if not self.visited[p]: # 방문 안했음 방문
                self.dfs(p)

def makeGraph(n, computers):
    graph = Graph(n)
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph.addEdge(i, j)
    return graph

def countSubTree(graph, n):
    count = 0
    for vtx in range(n):
        if not graph.visited[vtx]: # 방문 안했음
            graph.dfs(vtx) #방문 안된 vertex랑 연결된 것들은 다 방문함.
            count += 1  #방문이 안된 것은 연결이 안된 네트워크임.
    return count

def solution(n, computers):
    return countSubTree(makeGraph(n,computers), n)

"""### 첫번째 코드

- **알고리즘**
    - union-find 이용

- **시간 복잡도**
    - 각 노드를 연결하기 위한 이중 포문
        - O(n^2)
    - union작업은 비교연산이므로 상수시간,
    - find()하는 작업은 매 시점에서 최적화하여 상수시간임.
    - countSubTree는 각 정점의 루트 노드를 찾는 것으로 O(n)
    - 결론 O(n^2)

- **설명**
    - 결론적으로 서브트리의 개수를 세는 문제이므로, 루트 노드를 세면 됨.

### 두번째 코드

- 알고리즘
    - DFS
    - 자료구조 - 이미 문제에서 인접 행렬로 주어져서 구현할 필요는 없지만, 연습 겸 인접 리스트로 구현
    - 그래프를 구현해 DFS 탐색

- 시간 복잡도
    - 그래프를 만들기 위해서 2차원 배열로 주어진 인접행렬 각 정점을 추가
        - 이중 포문이므로 O(n^2)
    - dfs는 방문하지 않은 노드만 방문하므로, O(n)만큼 탐색

- 설명
    - 인접 리스트를 만들고, 0 정점부터 탐색하면서 이 정점과 연결된 모든 정점들을 하나의 네트워크로 카운팅함 count+=1
    - 이후 방문하지 않은 정점인 경우 마찬가지로, (연결되지 않은) 현 정점과 연결된 모든 정점을 방문한 뒤 count+1
        - 한마디로 연결된 정점들을 묶어서 하나로 카운팅하기 위해 방문하는 거임
        - 방문하면 방문 마킹을 하기 때문에 나중에 독립된 네트워크를 찾을 수 있음"""