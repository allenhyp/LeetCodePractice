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
    map<TreeNode*, TreeNode*> parent;
    vector<int> res;
    set<TreeNode*> visited;
    void findParent(TreeNode* node) {
        if (node) {
            if (node->left) {
                parent[node->left] = node;
                findParent(node->left);
            }
            if (node->right) {
                parent[node->right] = node;
                findParent(node->right);
            }
        }
    }
    
    void dfs(TreeNode* node, int K) {
        if (visited.find(node) == visited.end()) {
            visited.insert(node);
            if (K == 0) {
                res.push_back(node->val);
                return;
            }
            if (node->left) dfs(node->left, K - 1);
            if (node->right) dfs(node->right, K - 1);
            if (parent.find(node) != parent.end()) dfs(parent[node], K - 1);
        }
    }
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        findParent(root);
        dfs(target, K);
        return res;
    }
};
