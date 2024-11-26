import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class Graph{
    
    int[] roots;
    int[] heights;
    
    Graph(int size){
        this.roots = new int[size];
        this.heights = new int[size];
        
        for(int i=0 ;i<size; i++){
            this.roots[i] = i;
        }
    }
    
      
    public int find(int v){
        if(v == roots[v]) return v;
        roots[v] = find(roots[v]);
        return roots[v];
    }
    
    public  void union(int v1, int v2){
        int root1 = find(v1);
        int root2 = find(v2);
        
        if(heights[root1] == heights[root2]){
            this.roots[root1] = root2;
            this.heights[root2] += 1;
        }else if(heights[root1] < heights[root2]){
            this.roots[root1] = root2;
        }else{
            this.roots[root2] = root1;
        }
    }
    
    
    public String toString(){
        String root = Arrays.toString(this.roots);
        String height = Arrays.toString(this.heights);
        
        return root + " " + height;
        
    }
}


class Solution{
       public int solution(int n, int[][] computers){
        Graph g = new Graph(n);

        // 네트워크 구성
        for (int me = 0; me < computers.length; me++) {
            for (int other = me + 1; other < computers[me].length; other++) {
                if (computers[me][other] == 1) {
                    g.union(me, other);
                }
            }
        }
        // 카운트
        Set<Integer> uniqueRoots = new HashSet<>();
        for (int me = 0; me < n; me++) {
            uniqueRoots.add(g.find(me));
        }

        return uniqueRoots.size();
      }
}