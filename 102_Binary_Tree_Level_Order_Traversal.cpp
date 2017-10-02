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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > result;
        queue<TreeNode*> cur;
        cur.push(root);
        TreeNode *t;
        int levelSize = root? 1 : 0;
        while (levelSize > 0){
            vector<int> thisLevel;
            int i = levelSize;
            levelSize = 0;
            for (; i > 0; i--) {
                t = cur.front();
                thisLevel.push_back(t->val);
                if (t->left) {
                    cur.push(t->left);
                    levelSize++;
                }
                if (t->right) {
                    cur.push(t->right);
                    levelSize++;
                }
                cur.pop();
            }
            result.push_back(thisLevel);
        }
        return result;
    }
};
