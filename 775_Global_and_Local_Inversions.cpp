#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int n = A.size();
        for (int i = 0; i < n - 1; i++) {
            if (A[i] > A[i + 1] + 1 || i - A[i] > 1) {
                return false;
            }
        }
        if (n - 1 - A[n - 1] > 1) return false;
        return true;

    }
};

int main(void) {
    vector<int> A = {2,3,1,0};
    Solution mySolution;
    cout << mySolution.isIdealPermutation(A) << endl;
    return 0;
}
