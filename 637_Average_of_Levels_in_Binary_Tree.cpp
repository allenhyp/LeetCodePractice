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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<TreeNode*> queue;
        vector<double> res;
        queue.push_back(root);
        while (!queue.empty()) {
            vector<TreeNode*> next;
            double sum = 0;
            for (TreeNode* node : queue) {
                sum += node->val;
                if (node->left) next.push_back(node->left);
                if (node->right) next.push_back(node->right);
            }
            
            res.push_back(sum / queue.size());
            queue = next;
        }
        return res;
    }
};
