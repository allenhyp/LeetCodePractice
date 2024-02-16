struct compare{
    public:
    bool operator()(pair<string, int> &a, pair<string, int> &b)
    {
        if (a.second == b.second) return a.first < b.first;
        else return a.second > b.second;
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string, int> counter;
        priority_queue<pair<string, int>, vector<pair<string, int>>, compare> pq;
        for (string word : words) counter[word]++;
        for (auto freq : counter) {
            pq.push({freq.first, freq.second});
            if (pq.size() > k) pq.pop();
        }
        vector<string> res (k, "");
        while (k-- > 0) {
            res[k] = pq.top().first;
            pq.pop();
        }
        return res;
    }
};
