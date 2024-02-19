/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int maximum = INT_MIN;
    int dfs(TreeNode* node) {
        if (node == nullptr) return 0;
        int left = max(0, dfs(node->left));
        int right = max(0, dfs(node->right));
        maximum = max(maximum, node->val + left + right);
        return max(0, node->val + max(left, right));
    }
public:
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return maximum;
    }
};
