public class Harshad_number {
    public boolean solution(int x) {
        boolean answer = true;
        int x_len = (int) (Math.log10(x) + 1);
        int sum = 0;
        int tmp = x;

        if (tmp > 10) {
            sum += tmp / 10;
            tmp -= tmp / 10;
        } else if (tmp < 10) {
            sum += tmp;
        }
        System.out.println(sum);
        return answer;
    }
}