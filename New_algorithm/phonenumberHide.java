public class phonenumberHide {
    public String solution(String phone_number) {
        String answer = "";
        int phone_length = phone_number.length();
        // System.out.println(phone_length);

        String last_four = phone_number.substring(phone_length - 4);
        System.out.println(last_four);

        String secret_num = "*".repeat(phone_length - 4);
        // System.out.println(secret_num + last_four);
        answer = secret_num + last_four;
        return answer;
    }
}