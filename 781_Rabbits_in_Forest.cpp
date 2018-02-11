class Solution {
public:
    int numRabbits(vector<int>& answers) {
        if (answers.size() < 1) return 0;
        int result = 0;
        map<int, int> colorMap;
        map<int, int>::iterator it;
        for (int i = 0; i < answers.size(); i++) {
            int target = answers[i];
            it = colorMap.find(target);
            if (it == colorMap.end()) {
                colorMap[target] = 1;
            }
            else {
                colorMap[target] += 1;
            }
        }
        it = colorMap.find(0);
        if (it != colorMap.end()) {
            result += it->second;
            colorMap.erase(it);
        }
        for (auto& m : colorMap) {
            int base = m.second / (m.first + 1);
            if (m.second % (m.first+1)) base++;
            result += (m.first + 1) * base;
        }
        return result;
    }
};
