/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* ahead = dummy;
        ListNode* behind = dummy;
        while (ahead->next != NULL) {
            if (n-- <= 0) behind = behind->next;
            ahead = ahead->next;
        }
        ListNode* temp = behind->next;
        behind->next = behind->next->next;
        delete temp;
        return dummy->next;
    }
};
