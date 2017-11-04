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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return create(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
    }
    
    TreeNode* create(vector<int>& preorder, vector<int>& inorder, int preStart, int preEnd, int inStart, int inEnd) {
        if (preStart > preEnd) return NULL;
        TreeNode* node = new TreeNode(preorder[preStart]);
        int i = inStart;
        for (; i <= inEnd; i++) {
            if (inorder[i] == node->val)
                break;
        }
        node->left = create(preorder, inorder, preStart + 1, preStart + i - inStart, inStart, i - 1);
        node->right = create(preorder, inorder, preEnd + i - inEnd + 1, preEnd, i + 1, inEnd);
        return node;
    }
};
