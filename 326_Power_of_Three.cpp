#include <iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && (1162261467 % n == 0);
    }
};

int main(void) {
    Solution mySolution;
    int input = 0;
    cout << "INPUT: ";
    cin >> input;
    if (mySolution.isPowerOfThree(input)) cout << "RESULT: TRUE\n";
    else cout << "RESULT: FALSE\n";
    return 0;
}
