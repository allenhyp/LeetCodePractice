class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        long dvd = labs(dividend), dvs = labs(divisor), res = 0;
        while (dvd >= dvs) {
            long temp = dvs, m = 1;
            while (temp << 1 <= dvd) {
                temp <<= 1;
                m <<= 1;
            }
            
            dvd -= temp;
            res += m;
        }
        return (dividend > 0) == (divisor > 0) ? res : -res;
    }
};
