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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == NULL) return vector<int>();
        stack<TreeNode*> s;
        vector<int> result;
        s.push(root);
        TreeNode* t;
        while (!s.empty()) {
            t = s.top();
            result.push_back(t->val);
            s.pop();
            if (t->right) s.push(t->right);
            if (t->left) s.push(t->left);
        }
        return result;
    }
};
