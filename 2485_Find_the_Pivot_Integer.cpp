class Solution {
public:
    int pivotInteger(int n) {
        int prefix = int((n+2)*(n+1)/2);
        int postfix = 0;
        for (int i = n; i > 0; i--) {
            prefix -= i+1;
            postfix += i;
            if (prefix == postfix) return i;
        }
        return -1;
    }
};
