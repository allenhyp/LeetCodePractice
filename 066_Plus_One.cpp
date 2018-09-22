class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        digits[n]++;
        while (n >= 0) {
            if (digits[n] > 9) {
                digits[n] = 0;
                if (n != 0) digits[--n]++;
                else digits.insert(digits.begin(), 1);
            }
            else break;
        }
        return digits;
    }
};
