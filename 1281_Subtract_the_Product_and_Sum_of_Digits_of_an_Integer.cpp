class Solution {
public:
    int subtractProductAndSum(int n) {
        int prod = 1, sum = 0;
        while (n > 0) {
            int cur = n % 10;
            prod *= cur;
            sum += cur;
            n /= 10;
        }
        return prod - sum;
    }
};
