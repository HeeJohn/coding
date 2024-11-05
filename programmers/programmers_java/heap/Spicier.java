package programmers_java.heap;// 모든 음식의 스코빌 지수를 k 이상으로 만들기

// 가장 스코빌 지수가 작은 2가지 음식으로 새로운 스코빌 지수를 가진 음식

// 반복조건 : 모든 음식의 스코빌 지수가 k 이상이 될 때까지 반복 : 최소 힙의 root가 k 보다 작을 때

// 반복 횟수 카운트

import java.util.PriorityQueue;


class Spicier {
    public int solution(int[] scovilles, int k) {
        // data structure
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // init
        init(scovilles, minHeap);
        int count = 0;

        // process
        while (minHeap.peek() < k) {

            if (minHeap.size() < 2) return -1; // exception

            int leastSpicy = minHeap.poll();
            int secondLeastSpicy = minHeap.poll();

            int newScoville = makeNewScoville(leastSpicy, secondLeastSpicy);
            minHeap.offer(newScoville);
            count++;

        }

        return count;
    }

    private void init(int[] scovilles, PriorityQueue<Integer> minHeap) {
        for (int scoville : scovilles) {
            minHeap.offer(scoville);
        }
    }

    private int makeNewScoville(int first, int second) {
        return first + (second * 2);
    }
}
