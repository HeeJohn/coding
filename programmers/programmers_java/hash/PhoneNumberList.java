package programmers_java.hash;


import java.util.HashMap;


class PhoneNumberList {
    public boolean solution(String[] phone_book) {

        HashMap<String, Integer> map = new HashMap<>();

        for (String phone : phone_book) {
            map.put(phone, 0);
        }

        for (String phone : phone_book) {

            for (int i = 1; i < phone.length(); i++) {
                if (map.containsKey(phone.substring(0, i))) return false;
            }

        }

        return true;
    }
}