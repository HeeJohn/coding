package brute_force;


import java.util.Arrays;
import java.util.stream.IntStream;

class MockTest {
    public int[] solution(int[] answers) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int[] scores = new int[3];

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == a[i % a.length]) scores[0]++;
            if (answers[i] == b[i % b.length]) scores[1]++;
            if (answers[i] == c[i % c.length]) scores[2]++;
        }

        int maxScore = Arrays.stream(scores).max().orElse(0);

        return IntStream.range(0, scores.length)
                .filter(i -> scores[i] == maxScore)
                .map(i -> i + 1)
                .toArray();
    }
}

