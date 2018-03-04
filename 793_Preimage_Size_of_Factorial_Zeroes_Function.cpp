#include <iostream>
using namespace std;

class Solution {
public:
    int preimageSizeFZF(int K) {
        int left = 1, right = 1000000000;
        while (left < right) {
            int mid = (left + right) / 2;
            int k = cal(mid);
            if (k == K) return 5;
            else if (k > K) right = mid - 1;
            else left = mid + 1;
        }
        return 0;
    }
    
    int cal(int x) {
        int y = 5, ret = 0;
        while (x >= y) {
            ret += x / y;
            y *= 5;
        }
        return ret;
    }
};

int main(void) {
    Solution mySolution;
    cout << mySolution.preimageSizeFZF(55746) << endl;
    return 0;
}
