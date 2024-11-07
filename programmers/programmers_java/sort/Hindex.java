package programmers_java.sort;


// 발표한 논문 n편 중, h번 이상이 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용.

// 발표한 논문 n편 중, h번 이상이 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하 인용.


import java.util.Arrays;
import java.util.Comparator;

class Hindex {
    public int solution(int[] citations) {
        // 내림차순으로 정렬
        citations = Arrays.stream(citations)
                .boxed()
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue)
                .toArray();

        // h-Index 계산
        int hIndex = 0;
        for (int i = 0; i < citations.length; i++) {
            if (citations[i] >= i + 1) {
                hIndex = i + 1;
            } else {
                break;
            }
        }

        return hIndex;
    }
}
