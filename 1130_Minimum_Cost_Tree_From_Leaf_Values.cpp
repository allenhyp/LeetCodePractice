class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0;
        stack<int> s;
        s.push(INT_MAX);
        for (int a : arr) {
            while (s.size() > 1 && s.top() <= a) {
                int mid = s.top();
                s.pop();
                res += mid * min(s.top(), a);
            }
            s.push(a);
        }
        
        while (s.size() > 2) {
            int tmp = s.top();
            s.pop();
            res += tmp * s.top();
        }
        
        return res;
    }
};
