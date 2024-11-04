package programmers_java.stack;


// 기능은 진도가 100%일 때 서비스에 반영
// 각 기능은 개발 속도가 모두 다름

// 앞에 기능보다 뒤의 기능이 먼저 개발되더라도, 앞에 있는 기능이 배포될 때 함께 배포


import java.util.*;

class FeatureDevelopment {
    private static int done = 100;

    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();

        int days = 0;
        int counter = 1;
        for (int i = 0; i < progresses.length; i++) {
            int dayLeft = getDaysToBeDone(progresses[i], speeds[i]);

            // 현재 일수보다 작업하는 데 걸리는 일수가 작은 경우 담기
            // 현재 일수보다 작업하는 데 걸리는 일수가 크면, 새로운 package 저장.

            if (days < dayLeft) {
                days = dayLeft;
                counter = 1;
                list.add(counter);
            } else {
                list.set(list.size() - 1, ++counter);
            }
        }

        return list;
    }

    private int getDaysToBeDone(int progress, int speed) {
        return (int) Math.ceil((done - progress) / (double) speed);
    }
}