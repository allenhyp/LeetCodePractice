/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/
class Solution {
public:
    Node* inorderSuccessor(Node* node) {
        if (!node) return NULL;
        if (node->right) {
            Node* succ = node->right;
            while (succ->left)
                succ = succ->left;
            return succ;
        }
        int val = node->val;
        node = node->parent;
        while (node && val > node->val) node = node->parent;
        return node;
    }
};
