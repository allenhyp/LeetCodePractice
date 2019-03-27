#include "stdio.h"
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void reverseWords(vector<char>& str) { 
        for (int i = 0, j = 0; i <= str.size(); ++i) {
            if (i == str.size() || str[i] == ' ') {
                reverse(str.begin() + j, str.begin() + i);
                j = i + 1;
            }
        }
        reverse(str.begin(), str.end());
    }
};

int main() {
    Solution s;
    vector<char> str = {'t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'};
    s.reverseWords(str);
    for (char c : str) cout << c << ",";
    cout << endl;
    return 0;
};
