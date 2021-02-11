class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int maxSoFar = INT_MIN, maxHere = 0;
        int minSoFar = INT_MAX, minHere = 0;
        for (int num : nums) {
            maxHere += num;
            minHere += num;
            if (maxHere < 0) maxHere = 0;
            else if (maxSoFar < maxHere) maxSoFar = maxHere;
            if (minHere > 0) minHere = 0;
            else if (minSoFar > minHere) minSoFar = minHere;
        }
        
        return max(maxSoFar, -minSoFar);
    }
};
