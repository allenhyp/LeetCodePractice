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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL) return vector<int>();
        stack<TreeNode*> s;
        vector<int> result;
        TreeNode* t = root;
        while (!s.empty() || t) {
            if (t) {
                s.push(t);
                t = t->left;
            }
            else {
                TreeNode *p = s.top();
                result.push_back(p->val);
                s.pop();
                t = p->right;
            }
        }
        return result;
    }
};
