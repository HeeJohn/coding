package programmers_java.dp;

class OnTheWayHome {
    public int solution(int m, int n, int[][] puddles) {
        int[][] map = new int[n][m];
        map[0][0] = 1;

        for (int[] puddle : puddles) { // 물 웅덩이 마크
            int x = puddle[0];
            int y = puddle[1];

            map[y - 1][x - 1] = -1;
        }

        for (int y = 0; y < map.length; y++) {
            int[] row = map[y];

            for (int x = 0; x < row.length; x++) {
                if (row[x] == -1) {
                    row[x] = 0;
                    continue;
                }

                if (y > 0) {
                    row[x] += (map[y - 1][x]);
                }

                if (x > 0) {
                    row[x] += (map[y][x - 1]);
                }

                row[x] %= 1_000_000_007;
            }
        }

        return map[n - 1][m - 1];
    }

}