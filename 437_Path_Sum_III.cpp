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
public:
    int pathSum(TreeNode* root, int sum) {
        if (!root) return 0;
        return sumUp(root, 0, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
    
    int sumUp(TreeNode* root, int previous, int target) {
        if (!root) return 0;
        int current = previous + root->val;
        return (current == target) + sumUp(root->left, current, target) + sumUp(root->right, current, target);
    }
};
