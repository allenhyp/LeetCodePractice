/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        return toBST(head, NULL);
    }
    TreeNode* toBST(ListNode* head, ListNode* tail) {
        if (head == tail) return NULL;
        if (head->next == tail) {
            TreeNode* tRoot = new TreeNode(head->val);
            return tRoot;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast != tail && fast->next != tail) {
            fast = fast->next->next;
            slow = slow->next;
        }
        TreeNode* tRoot = new TreeNode(slow->val);
        tRoot->left = toBST(head, slow);
        tRoot->right = toBST(slow->next, tail);
        return tRoot;
    }
};

