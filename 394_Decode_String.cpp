#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        int i = 0;
        return decode(s, i);
    }
    string decode(string s, int& i) {
        string result = "";
        while (i < s.length() && s[i] != ']') {
            if (s[i] >= 'A') {
                result += s[i++];
            }
            else {
                int digit = 0;
                while (s[i] < 'A') {
                    digit *= 10;
                    digit += s[i] - '0';
                    i++;
                }
                ++i;
                string temp = decode(s, i);
                ++i;

                for (; digit > 0; digit--) {
                    result += temp;
                }
            }
        }
        return result;
    }
};
int main(void) {
    Solution mySolution;
    string input = "2[abc]3[cd]ef";
    cout << "Result: " << mySolution.decodeString(input) << endl;
    return 0;
}
