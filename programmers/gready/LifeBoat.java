package gready;

import java.util.Arrays;

class LifeBoat {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int left = 0;
        int right = people.length - 1;
        int count = 0;

        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                left++;
                right--;
                count++;
            } else {
                right--;
                count++;
            }
        }

        return count;
    }
}