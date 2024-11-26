import java.util.Queue;
import java.util.LinkedList;

class Robot {
    int[] pos;  
    int count;  

    Robot(int[] pos, int count) {
        this.pos = pos;
        this.count = count;
    }
}

class Solution {
    public int solution(int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;

        boolean[][] visited = new boolean[rows][cols];
        Queue<Robot> q = new LinkedList<>();
        q.add(new Robot(new int[]{0, 0}, 1));
        visited[0][0] = true;

        int[][] dirs = new int[][] {
            {0, 1},  
            {1, 0},  
            {0, -1}, 
            {-1, 0}  
        };

        while (!q.isEmpty()) {
            Robot curr = q.poll();


            int x = curr.pos[0]; // row
            int y = curr.pos[1]; // col


            if (x == rows - 1 && y == cols - 1) {
                return curr.count;
            }


            for (int[] dir : dirs) {
                int newX = x + dir[0];
                int newY = y + dir[1];

                if (inRange(newX, newY, maps) && !visited[newX][newY]) {
                    visited[newX][newY] = true;
                    q.add(new Robot(new int[] {newX, newY}, curr.count + 1));
                }
            }
        }

        return -1;
    }

    private boolean inRange(int x, int y, int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;
        return x >= 0 && x < rows && y >= 0 && y < cols && maps[x][y] == 1;
    }
}
