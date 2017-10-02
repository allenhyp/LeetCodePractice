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

class Solution {
public:
    vector<vector<int>> result;
    void builder(TreeNode* root, int depth) {
        if (root == NULL) return;
        if (result.size() == depth)
            result.push_back(vector<int>());
        result[depth].push_back(root->val);
        builder(root->left, depth+1);
        builder(root->right, depth+1);
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        builder(root, 0);
        return result;
    }
};
