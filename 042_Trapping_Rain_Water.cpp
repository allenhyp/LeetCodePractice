class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 3) return 0;
        int left = 0, right = height.size() - 1;
        int left_max = height[left], right_max = height[right], res = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] > left_max) left_max = height[left];
                else res += left_max - height[left];
                ++left;
            }
            else {
                if (height[right] > right_max) right_max = height[right];
                else res += right_max - height[right];
                --right;
            }
        }
        return res;
    }
};
