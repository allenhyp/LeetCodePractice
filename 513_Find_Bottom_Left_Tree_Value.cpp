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
    void recursive(TreeNode* node, int depth, int& left_val, int& max_depth) {
        // if (node == NULL) return;
        if (max_depth < depth) {
            left_val = node->val;
            max_depth = depth;
        }
        if (node->left) recursive(node->left, depth + 1, left_val, max_depth);
        if (node->right) recursive(node->right, depth + 1, left_val, max_depth);
    }
public:
    int findBottomLeftValue(TreeNode* root) {
        int max_depth = 1;
        int left_val = root->val;
        recursive(root, 1, left_val, max_depth);
        return left_val;
    }
};
