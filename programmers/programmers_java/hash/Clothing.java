package programmers_java.hash;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

class Clothing {
    public int solution(String[][] clothes) {

        HashMap<String, List<String>> clothesMap = new HashMap<>();

        for (String[] cloth : clothes) {
            String type = cloth[1];
            String name = cloth[0];

            List<String> clothesList = clothesMap.getOrDefault(type, new ArrayList<>());
            clothesList.add(name);
            clothesMap.put(type, clothesList);
        }

        int size = 1;

        for (Map.Entry<String, List<String>> entry : clothesMap.entrySet()) {
            size *= (entry.getValue().size() + 1);
        }

        return size - 1;
    }
}