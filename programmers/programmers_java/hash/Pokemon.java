package programmers_java.hash;

import java.util.HashSet;

public class Pokemon {
    public int solution(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        return Math.min(set.size(), nums.length / 2);
    }
}