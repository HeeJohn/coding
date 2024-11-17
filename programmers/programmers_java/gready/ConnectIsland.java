package programmers_java.gready;

// 최소 비용으로 모든 섬 통행
// 출력 : 최소 비용 return

// 여러 섬 건너도 연결되어 있으며 무방
//


// cost가 작은 순으로 정렬
// 연결 전 이미 연결된 섬인지 확인 (이 경우 continue)
// 연결되지 않은 경우 연결 후 root

// 모든 연결이 끝난 상태 즉 모든 root가 정해

import java.util.Arrays;
import java.util.Comparator;

class Graph{
    int[] roots;
    int[] depth;

    Graph(int n){
        this.roots = new int[n];
        this.depth = new int[n];
        init();
    }

    void init(){
        for(int i =0;i<roots.length;i++){
            this.roots[i]=i;
            this.depth[i] = 0;
        }
    }

    int find(int v){
        if(this.roots[v] == v) return v;

        this.roots[v] = find(this.roots[v]);

        return roots[v];
    }

    void union(int v1, int v2) {
        int root1 = find(v1); // 최상위 부모 찾기
        int root2 = find(v2);

        if (root1 != root2) { // 두 노드가 다른 집합에 있을 경우에만 병합
            if (this.depth[root1] < this.depth[root2]) {
                this.roots[root1] = root2;
            } else if (this.depth[root1] > this.depth[root2]) {
                this.roots[root2] = root1;
            } else {
                this.roots[root2] = root1;
                this.depth[root1]++; // 깊이를 증가시켜 균형 유지
            }
        }
    }



}

class ConnectIsland{
    public int solution(int n, int[][] costs){
        Arrays.sort(costs, Comparator.comparingInt((int[] i)-> i[2]));
        int min = 0;
        Graph g = new Graph(n);

        for(int[] cost : costs){
            if(g.find(cost[0]) != g.find(cost[1])){
                min += cost[2];
                g.union(cost[0], cost[1]);
                System.out.println(Arrays.toString(g.roots));
            }
        }

        return min;
    }
}
