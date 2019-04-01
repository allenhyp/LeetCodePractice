class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        vector<string> cur;
        int line = 0;
        for (string w : words) {
            if (line + cur.size() + w.size() > maxWidth) {
                for (int i = 0; i < maxWidth - line; ++i) {
                    cur[i % (cur.size() <= 1 ? 1 : (cur.size() - 1))] += ' ';
                }
                string sentance = "";
                for (string c : cur) sentance += c;
                sentance.substr(0, sentance.size() - 1);
                res.push_back(sentance);
                cur = vector<string>();
                line = 0;
            }
            cur.push_back(w);
            line += w.size();
        }
        string sentance = "";
        for (string c : cur) sentance += c + ' ';
        if (sentance.size() < maxWidth) 
            sentance += string(maxWidth - sentance.size(), ' ');
        res.push_back(sentance.substr(0, maxWidth));
        return res;
    }
};
