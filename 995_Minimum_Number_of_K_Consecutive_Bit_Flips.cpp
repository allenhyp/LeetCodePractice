class Solution {
public:
    int minKBitFlips(vector<int>& A, int K) {
        int flips = 0;
        int n = A.size();
        for (int i = 0; i < n - K + 1; i++) {
            if (A[i] == 0){
                for (int j = i; j < i + K; j++){
                    A[j] = A[j] == 0 ? 1 : 0;
                }
                flips++;
            }
        }
        for (int i = 0; i < n; i++){
            if (A[i] == 0) return -1;
        }
        return flips;
    }
};
