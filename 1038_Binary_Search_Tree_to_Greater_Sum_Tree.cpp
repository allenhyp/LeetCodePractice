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
    int sum = 0;
    void helper(TreeNode* node) {
        if (node == nullptr) return;
        helper(node->right);
        sum += node->val;
        node->val = sum;
        helper(node->left);
    }
public:
    TreeNode* bstToGst(TreeNode* root) {
        helper(root);
        return root;
    }
};
