class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        queue<int> positives;
        queue<int> negatives;
        vector<int> res;
        for (int num : nums) {
            if (num > 0) positives.push(num);
            else negatives.push(num);
        }
        while (!positives.empty() && !negatives.empty()) {
            res.push_back(positives.front());
            res.push_back(negatives.front());
            positives.pop();
            negatives.pop();
        }
        return res;
    }
};
