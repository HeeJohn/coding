package programmers_java.sort;


import java.util.Arrays;


class TheMostBigNum {
    public String solution(int[] numbers) {
        String[] numString = Arrays.stream(numbers)
                .mapToObj(Integer::toString)
                .toArray(String[]::new);

        Arrays.sort(numString, (o1, o2) -> {
            String s1 = o1 + o2;
            String s2 = o2 + o1;

            return s2.compareTo(s1);
        });

        if (numString[0].charAt(0) == '0') return "0";

        return String.join("", numString);
    }
}


// 성공률 60퍼인 코드...... 반례: [12, 121]

//import java.util.List;
//import java.util.LinkedList;
//import java.util.Arrays;
//import java.util.Collections;
//import java.util.Comparator;


//class Solution {
//    public String solution(int[] numbers) {
//        String[] numString = Arrays.stream(numbers)
//                .mapToObj(Integer::toString)
//                .toArray(String[]::new);
//
//        Arrays.sort(numString, new Comparator<String>() {
//            @Override
//            public int compare(String o1, String o2) {
//                int len1 = o1.length();
//                int len2 = o2.length();
//
//                int maxLength = Integer.max(len1, len2);
//
//                for (int i = 0; i < maxLength; i++) {
//                    char c1 = o1.charAt(Integer.min(i, len1 - 1));
//                    char c2 = o2.charAt(Integer.min(i, len2 - 1));
//
//                    if (c1 != c2) return Character.compare(c2, c1);
//                }
//
//                return o1.compareTo(o2);
//            }
//        });
//
//        return String.join("", numString);
//    }
//}
