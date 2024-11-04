package programmers_java.stack;
// 다리
// 트럭 최대 bridge_length 대
// 트럭 최대 weight 이하의 무게

// 완전히 올라야 카운팅


// 트럭이 올라가는 조건
// 1. currentW + incomingW <= maxW
// 2. currentTrucksNum + 1 <= bridge_length
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.AbstractMap;

class TruckOnBridge {
    public int solution(int bridge_length, int weight, int[] truck_weights){

        Queue<Map.Entry<Integer, Integer>> bridge = new LinkedList<>();
        int currentW = 0;
        int currentTrucksNum = 0;
        int seconds = 1;


        // 끝나는 조건
        int i =0;
        while(i < truck_weights.length){
            // 다리에서 벗어날 수 있는 트럭이 있는지 확인
            // 벗어나면, 다리에서 poll + 총 트럭에서 지나간 트럭 무게 빼기.
            if(!bridge.isEmpty()){
                int clockIn = bridge.peek().getKey();
                if(seconds - clockIn == bridge_length)
                    currentW -= bridge.poll().getValue();
            }

            int truckWeight = truck_weights[i];

            // 다리에 진입할 수 있는 트럭이 있는지 확인.
            // 진입 가능하면, truck 다리에 add, 트럭 무게 더하기.
            if(bridge.size() <= bridge_length && currentW+truckWeight <= weight ){
                currentW +=truckWeight;
                bridge.add(new AbstractMap.SimpleEntry(seconds, truckWeight));
                i++;
            }

            seconds++;
        }

        return seconds + bridge_length - 1;
    }
}