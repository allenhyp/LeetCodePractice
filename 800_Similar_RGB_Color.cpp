#include <iostream>
#include <sstream>
#include <string>
using namespace std;

class Solution {
public:
    int helper(string d2) {
        int temp, upper, upper2, lower, lower2, mid, mid2;
        temp = stoi(d2, 0, 16);
        upper = (temp + 0x10) >> 4;
        lower = (temp - 0x10) >> 4;
        mid = temp >> 4;
        if (upper > 0xf) {
            upper = 0xf;
            lower = 0xe;
        }
        if (lower < 0x0) {
            upper = 0x1;
            lower = 0x0;
        }
        upper2 = (upper << 4) + upper;
        lower2 = (lower << 4) + lower;
        mid2 = (mid << 4) + mid;
        if (abs(upper2 - temp) > abs(lower2 - temp)) {
            if (abs(mid2 -temp) > abs(lower2 - temp))
                return lower2;
            else return mid2;
        }
        else {
            if (abs(mid2 - temp) > abs(upper2 - temp))
                return upper2;
            else return mid2;
        }
    }
    string similarRGB(string color) {
        string result = "#";
        for (int i = 1; i < 7; i+=2) {
            stringstream ss;
            string s = "";
            s += color[i];
            s += color[i + 1];
            if (color[i] == color[i+1]) {
                result += s;
                continue;
            }
            ss << hex << setw(2) << setfill('0') << helper(s);
            result += ss.str();
        }
        return result;
    }
};

int main(void) {
    Solution my_solution;
    cout << my_solution.similarRGB("#98f1e3") << endl;
    return 0;
}
