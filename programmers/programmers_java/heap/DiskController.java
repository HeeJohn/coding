package programmers_java.heap;
// 작업 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리할 때 평균 구하기

// 작업 요청부터 종료까지의 평균을 줄이는 방법은 ?
// 1. 턴어라운드 타임을 줄여야 함 : turnaround time = completion time - requested time;
// 2. 여기서 requested time 은 주어지고, completion time은 다른 작업들로 인해 영향을 받는 변수.
// 3. completion time = waiting time + excution time(상수)

// ex :
// a : 0초에 요청, 100s 처리시간
// b : 1초에 요청, 90s 처리시간
// c : 100초에 요청, 10s 처리시간

// 1. a -> b -> c
// {100 + (190-1) + (200-100)} /3 = 129.67

// 2. a -> c -> b
// {100 + (110-100) + (200-1)} / 3 = 103


// 결론 : 무조건 excution time이 짧은 것으로 우선 실행해야 됨. (Shorest Job First)

// -------

// excution time 체크 시점 : 작업을 수행하지 않을 때 (이전 작업 완료 시점)
// 예외 : 완료 시점에 요청 작업이 없는 경우 먼저 요청이 들어온 것부터 처리
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Comparator;

class Job {
    private int requestedTime;
    private int executionTime;

    public Job(int rT, int eT) {
        this.requestedTime = rT;
        this.executionTime = eT;
    }

    public int getRequestedTime() {
        return this.requestedTime;
    }

    public int getExecutionTime() {
        return this.executionTime;
    }

    @Override
    public String toString() {
        return this.requestedTime + " " + this.executionTime;
    }
}

class DiskController {
    public int solution(int[][] jobs) {

        // data structure
        PriorityQueue<Job> requestQueue = new PriorityQueue<>(Comparator.comparingInt(Job::getRequestedTime));
        PriorityQueue<Job> jobMinHeap = new PriorityQueue<>(Comparator.comparingInt(Job::getExecutionTime));

        // init
        init(jobs, requestQueue);
        int totalResponseTime = 0;
        int currentTime = 0;

        // process jobs
        while (!requestQueue.isEmpty() || !jobMinHeap.isEmpty()) {

            // 요청 시간이 현재 시각 이하인 후보군들을 jobMinHeap에 추가
            putCandidateInQueue(requestQueue, jobMinHeap, currentTime);

            if (!jobMinHeap.isEmpty()) {
                // 실행 시간이 가장 짧은 작업을 수행
                Job nextJob = jobMinHeap.poll();
                int completionTime = getCompletionTime(currentTime, nextJob.getExecutionTime());
                totalResponseTime += getTurnaroundTime(nextJob.getRequestedTime(), completionTime);
                currentTime = completionTime; // 현재 시각 업데이트
            } else {
                // 작업을 기다려야 하는 경우, 다음 요청 시각으로 현재 시각을 업데이트
                if (!requestQueue.isEmpty()) {
                    currentTime = requestQueue.peek().getRequestedTime();
                }
            }
        }

        return totalResponseTime / jobs.length;
    }

    private void putCandidateInQueue( PriorityQueue<Job> requestQueue,  PriorityQueue<Job> jobMinHeap, int currentTime) {
        while (!requestQueue.isEmpty() && requestQueue.peek().getRequestedTime() <= currentTime) {
            jobMinHeap.offer(requestQueue.poll());
        }
    }

    private int getTurnaroundTime(int requestedTime, int completionTime) {
        return completionTime - requestedTime;
    }

    private int getCompletionTime(int startTime, int executionTime) {
        return startTime + executionTime;
    }

    private void init(int[][] jobs, PriorityQueue<Job> queue) {
        Arrays.sort(jobs, Comparator.comparingInt(job -> job[0]));
        for (int[] job : jobs) {
            queue.add(new Job(job[0], job[1]));
        }
    }
}
