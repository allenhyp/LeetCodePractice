class Solution {
private:
    map<string, int> parseFormula(string& formula, int& index) {
        map<string, int> counter;
        const int n = formula.size();
        while (index < n && formula[index] != ')') {
            auto cnt = parseUnit(formula, index);
            merge(counter, cnt, 1);
        }
        return counter;
    }

    map<string, int> parseUnit(string& formula, int& index) {
        map<string, int> counter;
        const int n = formula.size();
        if (formula[index] == '(') {
            auto cnt = parseFormula(formula, ++index);
            merge(counter, cnt, parseDigits(formula, ++index));
        } else {
            int start = index++;
            while (index < n && islower(formula[index])) ++index;
            string atom = formula.substr(start, index - start);
            int digits = parseDigits(formula, index);
            counter[atom] += digits;
        }
        return counter;
    }

    int parseDigits(string& formula, int& index) {
        int start = index;
        const int n = formula.size();
        while (index < n && isdigit(formula[index])) index++;
        return index == start ? 1 : stoi(formula.substr(start, index - start));
    }

    void merge(map<string, int>& a, map<string, int>& b, int multiplier) {
        for (auto const& [key, val] : b) a[key] += val * multiplier;
    }
public:
    string countOfAtoms(string formula) {
        int index = 0;
        auto result = parseFormula(formula, index);
        string ans = "";
        for (auto const& [key, val] : result)
            ans += key + (val > 1 ? to_string(val) : "");
        return ans;
    }
};
