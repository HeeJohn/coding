package programmers_java.sort;


// 발표한 논문 n편 중, h번 이상이 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용.

import java.util.Arrays;
import java.util.Comparator;

class Hindex {
    public int solution(int[] citations) {
        citations = Arrays.stream(citations)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();

        // 6 -> 5 -> 4 -> 3
        // 1 -> 2 -> 3 -> 4

        // 10 6 6 1 0
        // 1  2 3 4 5

        for (int i = 0; i < citations.length; i++) {

            if (i + 1 >= citations[i]) {
                return i;
            }
        }

        return citations.length;
    }
}
