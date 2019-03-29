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
    vector<int> boundaries;
    void leftBound(TreeNode* node) {
        if (!node || !node->left && !node->right) return;
        boundaries.push_back(node->val);
        if (node->left) leftBound(node->left);
        else leftBound(node->right);
    }
    
    void rightBound(TreeNode* node) {
        if (!node || !node->left && !node->right) return;
        if (node->right) rightBound(node->right);
        else rightBound(node->left);
        boundaries.push_back(node->val);
    }
    
    void leaves(TreeNode* node) {
        if (!node) return;
        else if (!node->left && !node->right) boundaries.push_back(node->val);
        else {
            leaves(node->left);
            leaves(node->right);
        }
    }
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        if (!root) return {};
        boundaries = vector<int> {root->val};
        leftBound(root->left);
        leaves(root->left);
        leaves(root->right);
        rightBound(root->right);
        return boundaries;
    }
};
