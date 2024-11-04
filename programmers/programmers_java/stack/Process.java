package programmers_java.stack;

import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.util.AbstractMap;


class Process {
    public int solution(int[] priorities, int location) {
        Queue<Map.Entry<Integer, Integer>> hashMapInQueue = new LinkedList<>();
        Map<Integer, Integer> priorityMap = new HashMap<>();

        // Init and find initial max priority
        int maxPriority = init(priorities, hashMapInQueue, priorityMap);

        // answer
        int counter = 1;

        // find
        while (!hashMapInQueue.isEmpty()) {
            Map.Entry<Integer, Integer> queueMapEntryEl = hashMapInQueue.poll();
            int currentTaskPriority = queueMapEntryEl.getValue();

            if (currentTaskPriority < maxPriority) {
                hashMapInQueue.add(queueMapEntryEl);
            } else {
                int currentTaskIndex = queueMapEntryEl.getKey();
                if (currentTaskIndex == location) return counter;

                // Update priority map and max priority
                updatePriorityMap(priorityMap, currentTaskPriority);
                if (currentTaskPriority == maxPriority) {
                    maxPriority = priorityMap.isEmpty() ? 0 : Collections.max(priorityMap.keySet());
                }
                counter++;
            }
        }

        return counter;
    }

    private int init(int[] priorities, Queue<Map.Entry<Integer, Integer>> queue, Map<Integer, Integer> priorityMap) {
        int maxPriority = 0;
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new AbstractMap.SimpleEntry<>(i, priorities[i]));
            priorityMap.put(priorities[i], priorityMap.getOrDefault(priorities[i], 0) + 1);
            maxPriority = Math.max(maxPriority, priorities[i]);
        }
        return maxPriority;
    }

    private void updatePriorityMap(Map<Integer, Integer> priorityMap, int priority) {
        int count = priorityMap.get(priority);
        if (count == 1) priorityMap.remove(priority);
        else priorityMap.put(priority, count - 1);
    }
}
