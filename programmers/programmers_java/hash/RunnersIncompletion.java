package programmers_java.hash;

import java.util.HashMap;
import java.util.Map;

class RunnersIncompletion {
    public String solution(String[] participants, String[] completions) {
        Map<String, Integer> comp = new HashMap<>();

        for (String completion : completions) {
            comp.put(completion, comp.getOrDefault(completion, 0) + 1);
        }

        for (String participant : participants) {
            int count = comp.getOrDefault(participant, 0) - 1;
            if (count < 0) {
                return participant; // 미완주자 발견 시 즉시 반환
            }
            comp.put(participant, count);
        }

        return ""; // 모든 참가자가 완주했을 경우 (주어진 문제 조건상 도달하지 않음)
    }
}
