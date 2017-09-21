class Solution {
public:
    int findNthDigit(int n) {
        long b = 9, d = 1;
        while (n - b * d > 0) {
            n -= b * d;
            b *= 10;
            d++;
        }
        int i = n % d;
        if (i == 0) i = d;
        long num = pow(10, d-1);
        num += (i == d) ? n / d - 1 : n / d;
        for (int k = i; k < d; k++) {
            num /= 10;
        }
        return num % 10;
    }
};
