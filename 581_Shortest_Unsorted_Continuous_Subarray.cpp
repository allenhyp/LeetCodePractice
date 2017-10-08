#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

// Stack
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int size = nums.size();
        if (nums.size() < 2) return 0;
        stack<int> sl;
        int lo = size;
        for (int i = 0; i < size; i++) {
            while (!sl.empty() && nums[sl.top()] > nums[i]) {
                lo = min(sl.top(), lo);
                sl.pop();
            }
            sl.push(i);
        }
        stack<int> sh;
        int hi = 0;
        for (int i = size - 1; i >= 0; i--) {
            while (!sh.empty() && nums[sh.top()] < nums[i]) {
                hi = max(sh.top(), hi);
                sh.pop();
            }
            sh.push(i);
        }
        return hi - lo <= 0 ? 0 : hi - lo + 1;
    }
};

// Iterative O(n) time and O(1) space
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int last = nums.size() - 1;
        if (nums.size() < 1) return 0;
        int start = -1, end = -2, Min = nums[last], Max = nums[0];
        for (int i = 1; i <= last; i++) {
            Max = max(Max, nums[i]);
            if (nums[i] < Max) end = i;
            Min = min(Min, nums[last - i]);
            if (nums[last - i] > Min) start = last - i;
        }
        return end - start + 1;
    }
};

int main(void) {
    vector<int> input = {1,2,3,4};
    Solution solution;
    cout << solution.findUnsortedSubarray(input) << endl;
    return 0;
}
