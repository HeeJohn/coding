package programmers_java.gready;

// 단속 카메라는 한번만

// 모든 차량이 카메라를 한번만 만나도록 하는 최소 카메라 수

import java.util.Arrays;
import java.util.Comparator;

// -20 -19 -18 -17 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3
//  |                |
//                       |                              |
//           |               |
//                                                      |      |
//       |   |
class SpeedCamera {

    public int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparingInt((int[] route) -> route[0]));
        int installed = 0;
        int tempInstalled = -300001;

        for (int[] route : routes) {

            if (route[0] > tempInstalled) { // 설치
                installed++;
                tempInstalled = route[1];
            }

            if (route[1] < tempInstalled) { // 조정
                tempInstalled = route[1];
            }

        }

        return installed;
    }
}