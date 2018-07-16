/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* this_node = head;
        while (this_node && this_node->next) {
            while (this_node->next && this_node->val == this_node->next->val) {
                this_node->next = this_node->next->next;
            }
            this_node = this_node->next;
        }
        return head;
    }
};
