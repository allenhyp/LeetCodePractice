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
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, NULL, NULL);
    }
    
    bool isValidBST(TreeNode* root, TreeNode* minNode, TreeNode* maxNode) {
        if (!root) return true;
        if (minNode && root->val <= minNode->val || maxNode && root->val >= maxNode->val) return false;
        return isValidBST(root->left, minNode, root) && isValidBST(root->right, root, maxNode);
    }
};
