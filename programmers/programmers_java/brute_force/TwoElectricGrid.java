package programmers_java.brute_force;

import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

class TwoElectricGrid {
    public int solution(int k, int[][] wires) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        makeGraph(wires, graph);

        int min = Integer.MAX_VALUE;

        for (int i = 0; i < wires.length; i++) {
            min = Integer.min(min, cut(wires[i], graph, k));
        }

        return min;

    }

    private int cut(int[] disconnected, Map<Integer, List<Integer>> graph, int k) {

        int first = bfs(graph, disconnected, k);
        int second = k - first;

        return Math.abs(first - second);
    }

    private int bfs(Map<Integer, List<Integer>> graph, int[] disconnected, int k) {
        boolean[] visited = new boolean[k + 1];
        Queue<Integer> q = new LinkedList<>();
        q.add(disconnected[0]);
        visited[disconnected[0]] = true;

        int count = 1;
        while (!q.isEmpty()) {
            int currentNode = q.poll();
            List<Integer> vertexs = graph.getOrDefault(currentNode, new LinkedList<>());

            for (Integer vertex : vertexs) {
                if (currentNode == disconnected[0] && vertex == disconnected[1] ||
                        currentNode == disconnected[1] && vertex == disconnected[0]) continue;
                if (visited[vertex]) continue;

                q.add(vertex);
                visited[vertex] = true;
                count++;
            }
        }
        return count;
    }

    private void makeGraph(int[][] wires, Map<Integer, List<Integer>> graph) {
        for (int[] wire : wires) {
            List<Integer> val1 = graph.getOrDefault(wire[0], new LinkedList<>());
            List<Integer> val2 = graph.getOrDefault(wire[1], new LinkedList<>());

            val1.add(wire[1]);
            graph.put(wire[0], val1);
            val2.add(wire[0]);
            graph.put(wire[1], val2);
        }
    }
}