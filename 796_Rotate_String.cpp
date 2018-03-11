#include <iostream>
using namespace std;

class Solution {
public:
    bool rotateString(string A, string B) {
        int a_size = A.size();
        int b_size = B.size();
        bool checked_once = false;
        if (a_size != b_size) return false;
        else if (a_size == 0) return true;
        int a_idx = 0, b_idx = 0;
        while(a_idx != a_size) {
            if (A[a_idx] == B[b_idx])
                a_idx++;
            else {
                b_idx -= a_idx;
                a_idx = 0;
            }
            b_idx++;
            if (b_idx == b_size) {
                if (a_idx != 0 && !checked_once) {
                    checked_once = true;
                    b_idx = 0;
                }
                else
                    return false;
            }
        }
        return true;
    }
};

int main(void) {
    Solution my_solution;
    string a = "slqhrmnxqjtyzvfldllvixbzpswspednzonqkjrlaltguusdxvknoasahjgqdquinucpmlxtdzpnmvxqtfwmxdqozgmaaycjebjs";
    string b = "llvixbzpswspednzonqkjrlaltguusdxvknoasahjgqdquinucpmlxtdzpnmvxqtfwmxdqozgmaaycjebjsslqhrmnxqjtyzvfld";
    cout << my_solution.rotateString(a, b) << endl;
    return 0;
}
