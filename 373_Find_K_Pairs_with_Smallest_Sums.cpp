class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int> > result;
        if (nums1.size() == 0 || nums2.size() == 0 || k == 0) return result;
        auto compare = [&nums1, &nums2](pair<int, int> a, pair<int, int> b) {
            return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
        }; // lambda in c++11, ([] is for variable capturing
        priority_queue<pair<int, int>, vector<pair<int, int> >, decltype(compare)> minHeap(compare);
        minHeap.emplace(0,0);
        while(k-- > 0 && minHeap.size()) {
            auto indexPair = minHeap.top(); minHeap.pop();
            // http://www.cplusplus.com/reference/vector/vector/emplace/
            // emplace is like insert and extend the size of the vector automatically.. sick..
            result.emplace_back(nums1[indexPair.first], nums2[indexPair.second]);
            if (indexPair.first + 1 < nums1.size())
                minHeap.emplace(indexPair.first + 1, indexPair.second);
            if (indexPair.first == 0 && indexPair.second + 1 < nums2.size())
                minHeap.emplace(indexPair.first, indexPair.second + 1);
        }
        return result;
    }
};
