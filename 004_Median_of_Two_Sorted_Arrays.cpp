class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        if (m > n) return findMedianSortedArrays(nums2, nums1);
        int left = 0, right = m, half_len = (m + n + 1) / 2;
        while (left <= right) {
            int partition1 = (left + right) / 2;
            int partition2 = half_len - partition1;
            int max_left_X = partition1 == 0 ? INT_MIN : nums1[partition1 - 1];
            int min_right_X = partition1 == m ? INT_MAX : nums1[partition1];
            int max_left_Y = partition2 == 0 ? INT_MIN : nums2[partition2 - 1];
            int min_right_Y = partition2 == n ? INT_MAX : nums2[partition2];
            if (max_left_X <= min_right_Y && max_left_Y <= min_right_X) {
                if ((m + n) % 2 == 0) return (max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2.0;
                else return max(max_left_X, max_left_Y);
            }
            else if (max_left_X > min_right_Y)
                right = partition1 - 1;
            else
                left = partition1 + 1;
        }
        return 0.0;
    }
};
