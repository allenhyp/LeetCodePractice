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
        if (!head || !head->next) return head;
        ListNode** runner = &head;
        while (*runner) {
            if ((*runner)->next && (*runner)->val == (*runner)->next->val) {
                while ((*runner)->next && (*runner)->val == (*runner)->next->val) {
                    *runner = (*runner)->next;
                }
                *runner = (*runner)->next;
            }
            else {
                runner = &((*runner)->next);
            }
        }
        return head;
    }
};
