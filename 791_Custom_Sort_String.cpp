class Solution {
public:
    string customSortString(string S, string T) {
        int iter = 0;
        char temp;
        for (int i = 0; i < S.size(); i++) {
            for (int j = iter; j < T.size(); j++) {
                if (S[i] == T[j]) {
                    temp = T[iter];
                    T[iter] = T[j];
                    T[j] = temp;
                    iter++;
                }
            }
        } 
        return T;
    }
};
