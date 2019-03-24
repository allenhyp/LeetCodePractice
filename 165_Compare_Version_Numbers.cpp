class Solution {
private:
    int levelRevision(string& version, int& index) {
        int level = 0;
        while (index < version.size() && version[index] != '.')
            level = level * 10 + (version[index++] - '0');
        index++;
        return level;
    }
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0;
        while (i < version1.size() || j < version2.size()) {
            int a = levelRevision(version1, i), b = levelRevision(version2, j);
            if (a > b) return 1;
            else if (a < b) return -1;
        }
        return 0;
    }
};
