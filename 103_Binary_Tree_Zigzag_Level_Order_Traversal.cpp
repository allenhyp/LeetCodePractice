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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == NULL) return vector<vector<int>>();
        vector<vector<int>> result;
        queue<TreeNode*> cur;
        cur.push(root);
        bool leftOrRight = true;
        while (!cur.empty()) {
            int levelSize = cur.size();
            vector<int> row(levelSize);
            for (int i = 0; i < levelSize; i++) {
                TreeNode *t = cur.front();
                int index = leftOrRight? i : (levelSize - i - 1);
                row[index] = t->val;
                cur.pop();
                if (t->left) cur.push(t->left);
                if (t->right) cur.push(t->right);
            }
            leftOrRight = !leftOrRight;
            result.push_back(row);
        }
        return result;
    }
};
