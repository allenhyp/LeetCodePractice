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
    vector<int> pt;
    void traverse(TreeNode* root) {
        if (root->left) traverse(root->left);
        pt.push_back(root->val);
        if (root->right) traverse(root->right);
    }
    bool isValidBST(TreeNode* root) {
        if (root) traverse(root);
        for (int i = 1; i < pt.size(); i++) {
            if (pt[i] <= pt[i-1]) return false;
        }
        return true;
    }
};
