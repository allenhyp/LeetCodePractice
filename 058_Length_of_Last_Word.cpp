class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1, result = 0;
        bool trailing = true;
        char target;
        for (int i = s.size() - 1; i >= 0; i--) {
            target = s[i];
            if ((target >= 'A' && target <= 'Z') || (target >= 'a' && target <= 'z')) {
                result++;
                trailing = false;
            }
            else if (trailing) continue;
            else break;
        }
        return result;
    }
};

class Solution {
public:
    int lengthOfLastWord(string s) {
        int result = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (isalpha(s[i])) result++;
            else {
                if (result > 0) {
                    return result;
                }
            }
        }
        return result;
    }
};
