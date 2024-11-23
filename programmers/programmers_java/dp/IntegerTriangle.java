package programmers_java.dp;

class IntegerTriangle {
    public int solution(int[][] triangle) {
        for (int i = triangle.length - 1; i > 0; i--) {
            int[] rowUnder = triangle[i];
            int[] rowTop = triangle[i - 1];

            for (int j = 0; j < rowTop.length; j++) {
                rowTop[j] += Integer.max(rowUnder[j], rowUnder[j + 1]);
            }
        }

        return triangle[0][0];
    }
}
