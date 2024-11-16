package gready;


// 바로 앞번호 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
// 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들을 수 있도록

// 입력 : 전체 학생의 수 n, 체육복을 도난  lost, 여분 reserve
// 출력 : 체육수업을 들을 수 있는 학생의 최댓값 return

// 특징 :
// 1. 있는 사람만 빌려줄 수 있음
// 2. 여벌 있는 사람도 도난 당할 수 있음(빌려줄 수 없음)

// 처리 :
// n 명 - (set(reserve) -set(lost)).size() 은 무조건 수업 들을 수 있음

import java.util.Set;
import java.util.LinkedHashSet;
import java.util.Arrays;

class PEClothing {
    public int solution(int n, int[] lost, int[] reserve) {
        // DS
        Set<Integer> lostSet = new LinkedHashSet<>();
        Set<Integer> reserveSet = new LinkedHashSet<>();

        // init
        init(lostSet, lost);
        init(reserveSet, reserve);
        Set<Integer> copySet = new LinkedHashSet<>(lostSet);
        lostSet.removeAll(reserveSet);
        reserveSet.removeAll(copySet);

        int count = n - lostSet.size();

        //process
        // [2, 4], [3, 5]
        // 3->2, 5->4

        // [2, 5],

        for (int ls : lostSet) {

            if (reserveSet.contains(ls - 1)) {
                reserveSet.remove(ls - 1);
                count++;
                continue;
            }

            if (reserveSet.contains(ls + 1)) {
                count++;
                reserveSet.remove(ls + 1);
            }
        }

        return count;
    }

    private void init(Set<Integer> set, int[] target) {
        Arrays.sort(target);
        for (int t : target) {
            set.add(t);
        }
    }
}



