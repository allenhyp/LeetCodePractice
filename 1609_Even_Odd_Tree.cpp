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
public:
    bool isEvenOddTree(TreeNode* root) {
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        int curr = -1, last = root->val;
        while (!q.empty()) {
            auto it = q.front(); q.pop();
            TreeNode* node = it.first;
            int level = it.second;
            
            if (node->val % 2 == level % 2) return false;
            if (level > curr) curr = level;
            else {
                if (level % 2 == 0 && node->val <= last) return false;
                if (level % 2 == 1 && node->val >= last) return false;
            }
            last = node->val;
            if (node->left != nullptr) q.push({node->left, level+1});
            if (node->right != nullptr) q.push({node->right, level+1});
        }
        return true;
    }
};
