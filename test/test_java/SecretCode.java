import java.util.*;

public class SecretCode {
        public static void main(String[] args) throws Exception {
            Scanner sc = new Scanner(System.in);
            String type = sc.next();
            String word = sc.next();
            int rotate = sc.nextInt();
            String target = sc.next();

            ArrayList<Integer> secretword = new ArrayList<>();
            ArrayList<Integer> targetword= new ArrayList<>();

            if(type.equals("encrypt")){
                encrypt(word, secretword, target, targetword, rotate);
            }else{
                decrypt(word, secretword, target, targetword, rotate);
            }

        }


    private static void encrypt(String word, ArrayList<Integer> secretword, String target, ArrayList<Integer> targetword, int rotate) {
        word.chars().forEach(value -> {
            secretword.add((value - (int) 'a')%26 );
        });
        target.chars().forEach(value -> {
            targetword.add((value - (int) 'a')%26);
        });

        Deque<Integer> q = new ArrayDeque<>();
        for(int i = 0; i< secretword.size(); i++){
            q.add((targetword.get(i) +secretword.get(i))%26);
        }

        if (rotate >0) {
            for (int i = 0; i < Math.abs(rotate); i++){
                q.addLast(q.pollFirst());
            }
        }else{
            for (int i = 0; i < Math.abs(rotate); i++) {
                q.addFirst(q.pollLast());
            }
        }

        StringBuilder answer = new StringBuilder();
        while (!q.isEmpty()) {
            int t = q.pollFirst();
            answer.append((char) ('a'+t));
        }
        System.out.println(answer);
    }

    private static void decrypt(String word, ArrayList<Integer> secretword, String target, ArrayList<Integer> targetword, int rotate) {
        word.chars().forEach(value -> {
            secretword.add((value - (int) 'a')%26 );
        });

        Deque<Integer> q = new ArrayDeque<>();
        target.chars().forEach(value -> {
            q.add((value - (int) 'a')%26);
        });

        if (rotate <0) {
            for (int i = 0; i < Math.abs(rotate); i++){
                q.addLast(q.pollFirst());
            }
        }else{
            for (int i = 0; i < Math.abs(rotate); i++) {
                q.addFirst(q.pollLast());
            }
        }
        System.out.println(q);
        while (!q.isEmpty()) {
            targetword.add(q.pollFirst());
        }

        for(int i = 0; i< secretword.size(); i++){
            int input = targetword.get(i) - secretword.get(i);
            if (input<0) {
                input= 26+input;
            }
            q.add(input);
        }
        System.out.println(q);
        StringBuilder answer = new StringBuilder();
        while (!q.isEmpty()) {
            int t = q.pollFirst();
            answer.append((char) ('a' + t));
        }

        System.out.println(answer);
    }

}
