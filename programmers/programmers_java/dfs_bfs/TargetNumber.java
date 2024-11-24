package programmers_java.dfs_bfs;

import java.util.HashMap;
import java.util.Map;

class TargetNumber {

    public int solution(int[] numbers, int target) {
        Map<String, Integer> memo = new HashMap<>();
        return dfs(numbers, 0, 0, target, memo);
    }

    private int dfs(int[] numbers, int index, int currentSum, int target, Map<String, Integer> memo) {
        System.out.println(memo);
        if (index == numbers.length) {
            return currentSum == target ? 1 : 0;
        }

        String key = index + "," + currentSum;

        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int add = dfs(numbers, index + 1, currentSum + numbers[index], target, memo);
        int subtract = dfs(numbers, index + 1, currentSum - numbers[index], target, memo);

        // 결과를 캐시에 저장
        memo.put(key, add + subtract);

        return add + subtract;
    }
}
