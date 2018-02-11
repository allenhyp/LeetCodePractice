/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    void traversal(TreeNode* node, vector<int>& nums) {
        if (node != NULL) {
            traversal(node->left, nums);
            nums.push_back(node->val);
            traversal(node->right, nums);
        }
        return;
    }

public:
    int minDiffInBST(TreeNode* root) {
        vector<int> nums = {};
        traversal(root, nums);
        int minimum = INT_MAX;
        for (int i = 1; i < nums.size(); i++) {
            minimum = min(minimum, nums[i] - nums[i - 1]);
        }
        return minimum;
    }
};
