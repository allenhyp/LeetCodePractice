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
    vector<vector<int>> result;
    void traverse(TreeNode* node, int sum, vector<int>& current) {
        vector<int> newCur = current;
        newCur.push_back(node->val);
        if (!(node->left || node->right)) {
            for (int i = 0; i < newCur.size(); i++)
                sum -=  newCur[i];
            if (sum == 0)
                result.push_back(newCur);
        }
        else {
            if (node->left)
                traverse(node->left, sum, newCur);
            if (node->right)
                traverse(node->right, sum, newCur);
        }
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if (root == NULL) return result;
        vector<int> cur;
        traverse(root, sum, cur);
        return result;
    }
};
