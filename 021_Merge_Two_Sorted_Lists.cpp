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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        dummy->next = l1;
        while (l1 && l2) {
            if (l1->val < l2->val)
                l1 = l1->next;
            else {
                ListNode* tmp = l2->next;
                cur->next = l2;
                l2->next = l1;
                l2 = tmp;
            }
            cur = cur->next;
        }
        if (l2) cur->next = l2;
        return dummy->next;
    }
};
