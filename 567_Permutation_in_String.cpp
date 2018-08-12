class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int size1 = s1.length(), size2 = s2.length();
        if (size1 > size2) return false;
        vector<int> v1(26, 0), v2(26, 0);
        for (int i = 0; i < size1; i++)
            v1[s1[i] - 'a']++;    
        for (int i = 0; i < size2; i++) {
            if (i >= size1) v2[s2[i - size1] - 'a']--;
            v2[s2[i] - 'a']++;
            if (i >= size1 -1 && v1 == v2) return true;
        }
        return false;
    }
};
