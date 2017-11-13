#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

class Solution {
private:
    map<string, int> parseFormula(string& s, int& i) {
        map<string, int> counts;
        const int n = s.size();
        while (i < n && s[i] != ')') {
            map<string, int> cnts = parseUnit(s, i);
            merge(counts, cnts, 1);
        }
        return counts;
    }

    map<string, int> parseUnit(string& s, int& i) {
        map<string, int> counts;
        const int n = s.size();
        if (s[i] == '(') {
            map<string, int> cnts = parseFormula(s, ++i);
            int digits = parseDigits(s, ++i);
            merge(counts, cnts, digits);
        }
        else {
            int i0 = i++;
            while (i < n && s[i] >= 'a' && s[i]<= 'z') i++;
            string atom = s.substr(i0, i - i0);
            int digits = parseDigits(s, i);
            counts[atom] += digits;
        }
        return counts;
    }

    int parseDigits(string& s, int&i) {
        int d = 0;
        while (i < s.size() && s[i] >= '0' && s[i] <= '9') {
            d *= 10;
            d += s[i] - '0';
            i++;
        }
        return d == 0? 1 : d;
    }

    void merge(map<string, int>& m1, map<string, int>& m2, int times) {
        for (pair<string, int> p : m2) m1[p.first] += p.second * times;
    }
public:
    string countOfAtoms(string formula) {
        string output = "";
        int i = 0;
        map<string, int> counts = parseFormula(formula, i);
        for (pair<string, int> p : counts) {
            output += p.first;
            if (p.second > 1) output += to_string(p.second);
        }
        return output;
    }
};

int main(void) {
    string input = "Mg(OH)2";
    Solution mySolution;
    cout << mySolution.countOfAtoms(input) << endl;
    return 0;
}
