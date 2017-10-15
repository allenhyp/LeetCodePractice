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
    vector<int> result;
    long curVal = INT_MAX-1;
    int curCount = 1;
    int maxCount = 0;
    int modeCount = 0;
    void inorder(TreeNode* t) {
        if (t == NULL) return;
        inorder(t->left);
        if (curVal == t->val) curCount++;
        else curCount = 1;
        if (curCount > maxCount) {
            maxCount = curCount;
            result = vector<int>();
            result.push_back(t->val);
        }
        else if (curCount == maxCount) {
            result.push_back(t->val);
        }
        curVal = t->val;
        inorder(t->right);
    }
public:
    vector<int> findMode(TreeNode* root) {
        if (root == NULL) return vector<int>();
        inorder(root);
        return result;
    }
};
