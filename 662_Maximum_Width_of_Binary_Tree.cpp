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
    int dfs(TreeNode* root, int level, int order, vector<pair<int, int>> &record) {
        if (root == NULL) return 0;
        if (record.size() == level) record.push_back({order, order});
        else record[level].second = order;
        return max({record[level].second - record[level].first + 1,
                    dfs(root->left, level + 1, order * 2, record),
                    dfs(root->right, level + 1, order * 2 + 1, record)});
    }
    int widthOfBinaryTree(TreeNode* root) {
        return dfs(root, 0, 1, vector<pair<int, int>>() = {});
    }
};
