class Solution {
private:
    vector<string> parse(string s) {
        vector<string> res;
        string delimiter = ":";
        size_t pos = 0;
        while ((pos = s.find(delimiter)) != string::npos) {
            res.push_back(s.substr(0, pos));
            s.erase(0, pos + delimiter.length());
        }
        res.push_back(s);
        return res;
    }
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res (n, 0);
        stack<int> record;
        int prev = 0;
        for (string log : logs) {
            vector<string> items = parse(log);
            int id = stoi(items[0]), time = stoi(items[2]);
            if (!record.empty()) res[record.top()] += time - prev;
            prev = time;
            if (items[1] == "start") record.push(id);
            else {
                res[record.top()]++;
                record.pop();
                prev++;
            }
        }
        return res;
    }
};
