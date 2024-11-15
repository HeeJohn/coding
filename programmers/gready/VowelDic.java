package gready;


// dfs
class VowelDic {
    int count = 0;

    public int solution(String word) {
        char[] alph = {'A', 'E', 'I', 'O', 'U'};

        findWordInComb(word, "", alph);

        return count;
    }

    private boolean findWordInComb(String word, String prefix, char[] alph) {
        System.out.println(prefix);
        if (prefix.equals(word)) return true;
        // 5글자 안되면, 글자수부터 늘리기
        // 5글자 되면, 전환

        if (prefix.length() < alph.length) {
            for (int i = 0; i < alph.length; i++) {
                count++;
                if (findWordInComb(word, prefix + alph[i], alph)) return true;
            }
        }

        return false;
    }


}