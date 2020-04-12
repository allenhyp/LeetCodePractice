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
    int diameterOfBinaryTree(TreeNode* root) {
        int maximum = 0;
        traverse(root, maximum);
        return maximum;
    }
private:
    int traverse(TreeNode* node, int& maximum) {
        if (!node) return 0;
        int left = traverse(node->left, maximum);
        int right = traverse(node->right, maximum);
        maximum = max(maximum, left + right);
        return 1 + max(left, right);
    }
};
