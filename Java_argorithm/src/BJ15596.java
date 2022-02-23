public class BJ15596 {

    public static void main(String[] args) {
        int[] a = new int[10];

        long ans = BJ15596.sum(a);
    }

    private static long sum(int[] a) {

        long ans = 0;
        for (int i : a){
            ans += i;
        }
        return ans;
    }

}

// 시간 복잡도 O(n)
// 공간 복잡도 O(1)
