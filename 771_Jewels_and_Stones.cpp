#include <iostream>
#include <map>
#include <string>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        map<char, bool> jewels;
        for (int i = 0; i < J.size(); i++) {
            jewels[J[i]] = true;
        }
        int result = 0;
        for (int i = 0; i < S.size(); i++) {
            if (jewels[S[i]]) result++;
        }
        return result;
    }
};

int main(void) {
    string J = "b";
    string S = "aAAbbbb";
    Solution mySolution;
    cout << "Result = " << mySolution.numJewelsInStones(J, S) << endl;
    return 0;
}
