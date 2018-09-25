class Solution {
public:
    bool checkValidString(string s) {
        stack<char> s1, s2;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ')') {
                bool pass = false;
                while (!s1.empty()) {
                    if (s1.top() == '*') {
                        s2.push('*');
                        s1.pop();
                    }
                    else {
                        s1.pop();
                        pass = true;
                        break;
                    }
                }
                if (!pass) {
                    if (s2.empty()) return false;
                    else s2.pop();
                }
                while (!s2.empty()) {
                    s1.push(s2.top());
                    s2.pop();
                }
            }
            else s1.push(s[i]);
        }
        // stack<char> s3;
        // while (!s1.empty()) {
        //     cout << s1.top() << ' ';
        //     s2.push(s1.top());
        //     s1.pop();
        // }  
        while (!s1.empty()) {
            if (s1.top() == '*'){
                s2.push(s1.top());
                s1.pop();
            }
            else if (!s2.empty()) {
                s2.pop();
                s1.pop();
            }
            else return false;
        }
        return true;
    }
};
