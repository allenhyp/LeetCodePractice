class Solution {
private:
    bool checkPalindrome(string word) {
        int left = 0, right = word.size()-1;
        while (left < right) {
            if (word[left++] != word[right--]) return false;
        }
        return true;
    }
public:
    string firstPalindrome(vector<string>& words) {
        for (string word : words) {
            if (checkPalindrome(word)) return word;
        }
        return "";
    }
};
