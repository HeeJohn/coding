package brute_force;

// 가로 길이 >= 세로 길이
// brown이 겉, yellow 속


// 가로 * 세로 = brown * yellow
// 24
// (2, 12), (3, 8), (4, 6), (5)

import java.util.LinkedList;
import java.util.Map;
import java.util.AbstractMap;
import java.util.List;

class Carpet {

    public int[] solution(int brown, int yellow) {
        List<Map.Entry<Integer, Integer>> comb = new LinkedList<>();

        findComb(comb, yellow);

        return findMatch(comb, brown);
    }

    private int[] findMatch(List<Map.Entry<Integer, Integer>> comb, int brown) {

        for (Map.Entry<Integer, Integer> entry : comb) {
            int height = entry.getKey();
            int width = entry.getValue();

            if (2 * (width + 2) + (height + 2) * 2 - 4 == brown) {
                return new int[]{width + 2, height + 2};
            }
        }

        return new int[2];
    }


    private void findComb(List<Map.Entry<Integer, Integer>> comb, int yellow) {
        for (int i = 1; i <= Math.sqrt(yellow); i++) {
            if (yellow % i == 0) {
                comb.add(new AbstractMap.SimpleEntry<Integer, Integer>(i, yellow / i));
            }
        }
    }
}