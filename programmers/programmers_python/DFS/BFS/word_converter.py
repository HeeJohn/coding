

# 1. 그래프를 만들때 target이 words 안에 있는지 확인.
# 2. 그래프는 인접리스트로 구현 
# 이어질 수 있는 글자 (교집합이 글자수 -1 or 차집합이 1 )에 대해 인덱스값을 가지고 있도록. 
# 3. 최단거리는 depth로 탐


from collections import deque

class Graph :
    def __init__(self, words) :
        self.adjList = [[] for _ in range(len(words))]
        self.visited = [False]*len(words)
        self.words = words
    
    def addVertex(self, v, u) :
        self.adjList[v].append(u)
        self.adjList[u].append(v)
    
    def bfs(self, i, target) :
        queue = deque([(i,0)])
        
        while queue :
            i, count = queue.popleft()
            self.visited[i] = True
            
            if target == self.words[i] :
                return count
            
            for v in self.adjList[i] :
                if not self.visited[v] :
                    queue.append((v, count+1))
        
                
def isConnected(w1, w2):
    diff_count = 0
    
    for char1, char2 in zip(w1, w2):
        if char1 != char2:
            diff_count += 1
            if diff_count > 1:
                return False
    
    return diff_count == 1
                
                
def makeGraph(words) :
    graph = Graph(words)
    
    for i in range(len(words)-1) :
        for j in range(i+1, len(words)) :
            if isConnected(words[i], words[j]) :
                graph.addVertex(i, j)
    return graph
    
def solution(begin, target, words):
    
    #1.target이 words안에 존재하는지 먼저 파악
    if not target in words :
        return 0
    
    words.append(begin)
    graph = makeGraph(words)
    
    for node in graph.adjList :
        print(node)
    
    return graph.bfs(-1, target)


print(solution("aab", "aba", ["abb","aba"]))

