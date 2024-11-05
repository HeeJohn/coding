package programmers_java.heap;


// 연산 후 큐 상태에 따라 [0,0] | [최댓값, 최솟값]

// 명령어
// I insert : 숫자 삽입
// D delete : (2개 일때 하나만 삭제, 비어있을 때 무시)
// 양수 : 최댓값 삭제
// 음수 : 최솟값 삭제

import java.util.LinkedList;
import java.util.List;
import java.util.Collections;

class DoublePriorityQueue{
    public int[] solution(String[] operations){
        // Data structure
        List<Integer> list = new LinkedList<>();

        for(String opr : operations){

            String[] container = opr.split(" ");
            Integer num = Integer.parseInt(container[1]);

            if(container[0].equals("I")){
                // I insert : 숫자 삽입

                int index = Collections.binarySearch(list, num);
                if(index < 0 ){
                    index = -(index+1);
                }
                list.add(index, num);

            }else if(!list.isEmpty()) {
                // D delete : (2개 일때 하나만 삭제, 비어있을 때 무시)

                if(num>0){
                    list.remove(list.size()-1);
                }else{
                    list.remove(0);
                }
            }
        }

        //process



        // result
        if(list.isEmpty()) return new int[]{0,0};

        return new int[]{list.get(list.size()-1), list.get(0)};
    }


}




//
//
//import java.util.TreeMap;
//
//class DoublePriorityQueue {
//    public int[] solution(String[] operations) {
//        // TreeMap 사용: 키는 값, 값은 빈도수
//        TreeMap<Integer, Integer> map = new TreeMap<>();
//
//        for (String opr : operations) {
//            String[] container = opr.split(" ");
//            int num = Integer.parseInt(container[1]);
//
//            if (container[0].equals("I")) {
//                // 숫자 삽입: 기존 빈도수에서 +1
//                map.put(num, map.getOrDefault(num, 0) + 1);
//            } else if (!map.isEmpty()) {
//                // D 명령어 처리: 최댓값 또는 최솟값 삭제
//                int key = (num > 0) ? map.lastKey() : map.firstKey();
//                if (map.get(key) == 1) {
//                    map.remove(key); // 빈도수가 1인 경우 키 제거
//                } else {
//                    map.put(key, map.get(key) - 1); // 빈도수 감소
//                }
//            }
//        }
//
//        // 결과 처리
//        if (map.isEmpty()) return new int[]{0, 0};
//
//        // 최댓값과 최솟값 반환
//        return new int[]{map.lastKey(), map.firstKey()};
//    }
//}
