"""Description
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
입출력 예 설명

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다."""




## 첫번째 코드 -> 정확도 25퍼 
## 그리디하지만, 연결성 보장이 안됨.


def solution(n, costs):
    visited =[]
    costs.sort(key=lambda x : x[2])
    money = 0
    
    
    for cost in costs : 
        vtx1 = cost[0]
        vtx2 = cost[1]
        
        if vtx1 in visited and vtx2 in visited : 
            continue
        
        if vtx1 not in visited :
            visited.append(vtx1)
            
        if vtx2 not in visited :
            visited.append(vtx2)
            
        money+= cost[2]
        
        if len(visited) == n : 
            return money
    
    return money


## 2번째 코드 
## 비슷한 방법이지만 연결성을 보장하는 kruskal알고리즘
## union을 이용하여 사이클을 형성하지 않는 간선은 포함하여 집합을 만듬.
## 사이클을 형성하지 않음을 root 노드를 통해 파악
## 1번 코드와 같은 방법으로 가장 가중치가 낮은 간선부터 차례대로 선택함.

class Tree:
    def __init__(self, n):
		    #각 노드들의 부모 정점리스트
		    # 처음은 각 정점의 루트는 본인
        self.parent = list(range(n)) 
        self.depth = [0] * n # 트리깊이 
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 
		
    def union(self, root_v1, root_v2):
		    #큰 쪽에 작은 것을 붙이기
        if self.depth[root_v1] < self.depth[root_v2]:
            self.parent[root_v1] = root_v2 #작은 것의 루트노드를 큰 것의 루트로 변경
        elif self.depth[root_v1] > self.depth[root_v2]:
            self.parent[root_v2] = root_v1
        else: 
            self.parent[root_v2] = root_v1 #같은 경우 아무거나.
            self.depth[root_v2] += 1

def solution(n, costs):
    costs.sort(key=lambda x: x[2]) 
    tree = Tree(n)
    total = 0
    
    #신장트리는 n-1로 구성되어 있으나 여기서 e가 
    # (n-1)*n/2로 n-1에 비해 작으므로, 간선의 개수만 이용.
    for vtx1, vtx2, cost in costs: 
    
        root_v1 = tree.find(vtx1)
        root_v2 = tree.find(vtx2)
        
        #spanning tree를 만족하는지 확인    
        if root_v1 != root_v2:
            tree.union(root_v1, root_v2) #현재 노드들의 집합(서브트리) 합치기
            total += cost
            
    return total
    


"""    - Kruskal 알고리즘
    - 최소비용 신장트리 → 즉 사이클이 생성되지 않는 신장트리를 최소비용의 간선들로 구성
    - costs로 주어지는 것은 결국 간선들 → [출발지, 목적지, 가중치]
    - 간선의 가중치로 정렬해 최소 간선을 선택하면서, 신장트리를 형성할 수 있도록 한다.
    
- 시간 복잡도
    - n은 정점, e는 간선일 때, 조건에서 e는 (n-1)*n/2 이하라고 주어짐.
    - 간선을 가중치에 따라 정렬
        - O(eloge)
    - 간선에 붙어 있던 노드들의 루트 정점을 찾기
        - 하나의 서브트리에 포함된 모든 정점들의 부모를 루트로 갱신(최적화)해주고 있기 때문에 O(1)
    - 주어진 간선을 모두 순회하면서 사이클이 생기지 않게 연결하기
        - e만틈 순환 O(e)
    - 결론적으로 O(eloge)"""