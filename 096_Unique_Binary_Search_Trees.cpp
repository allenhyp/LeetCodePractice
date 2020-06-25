// Greedy
class Solution {
public:
    int numTrees(int n) {
        if (n <= 1) return 1;
        unsigned int result = 0;
        for (int i = 0; i < n; i++) {
            result += numTrees(i) * numTrees(n - i - 1);
        }
        return result;
    }
};

// Dynamic Programming
class Solution {
public:
    int numTrees(int n) {
        unsigned long catalan[n + 1];
        catalan[0] = 1, catalan[1] = 1;
        for (int i = 2; i <= n; i++) {
            catalan[i] = 0;
            for (int j = 0; j < i; j++) {
                catalan[i] += catalan[j] * catalan[i-j-1];
            }
        }
        return catalan[n];
    }
};
