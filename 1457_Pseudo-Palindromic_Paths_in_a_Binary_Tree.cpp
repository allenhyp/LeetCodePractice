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
    int traverse (TreeNode* node, int count) {
        if (!node) return 0;
        count ^= 1 << (node->val - 1);
        int res = traverse(node->left, count) + traverse(node->right, count);
        if (!node->left && !node->right && (count & (count - 1)) == 0) res++;
        return res;
    }

public:
    int pseudoPalindromicPaths (TreeNode* root) {
        return traverse(root, 0);
    }
};
