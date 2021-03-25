class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> AB;
        int res = 0;
        for (int a : A) {
            for (int b : B) {
                AB[a + b] += 1;
            }
        }
        
        for (int c : C) {
            for (int d : D) {
                res += AB[-c - d];
            }
        }
        
        return res;
    }
};
