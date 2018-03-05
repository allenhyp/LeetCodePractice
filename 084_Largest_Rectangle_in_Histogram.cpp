#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ret = 0;
        vector<int> index;
        heights.push_back(0);
        for (int i = 0; i < heights.size(); i++) {
            while (index.size() > 0 && heights[index.back()] >= heights[i]) {
                int h = heights[index.back()];
                index.pop_back();
                int s = index.size() > 0 ? index.back() : -1;
                if (h * (i - s - 1) > ret) {
                    ret = h * (i - s - 1);
                }
            }
            index.push_back(i);
        }
        return ret;
    }
};

int main(void) {
    Solution my_solution;
    vector<int> input = {2,1,5,6,2,3};
    cout << my_solution.largestRectangleArea(input) << endl;
    return 0;
}
