class Solution {
public:
    int calculate(string s) {
        stack<int> stk;
        int num = 0;
        int temp = 0;
        char sign = '+';

        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (c >= '0') num = num * 10 + (c - '0');
            if (c < '0' && c != ' ' || i == s.size() - 1) {
                switch (sign) {
                    case '+':
                        stk.push(num);
                        break;
                    case '-':
                        stk.push(-num);
                        break;
                    case '*':
                        temp = stk.top(); stk.pop();
                        stk.push(temp * num);
                        break;
                    case '/':
                        temp = stk.top(); stk.pop();
                        stk.push(temp / num);
                        break;
                }
                sign = c;
                num = 0;
            }
        }
        
        int res = 0;
        while (!stk.empty()) {
            res += stk.top();
            stk.pop();
        }
        return res;
    }
};
