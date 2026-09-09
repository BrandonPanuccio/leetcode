class Solution {
    public int countCommas(int n) {
        return n < 1000 ? 0 : n - 999;
    }
}

class Test {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.countCommas(1002);
        System.out.println(result);
    }
}