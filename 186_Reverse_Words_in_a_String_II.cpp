#include "stdio.h"
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void reverseWords(vector<char>& str) { 
        reverse(str.begin(), str.end());
        for (auto i = str.begin(), j = i; i < str.end(); i = j + 1) {
            for (j = i; j < str.end() && *j != ' '; ++j);
            reverse(i, j);
        }
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
