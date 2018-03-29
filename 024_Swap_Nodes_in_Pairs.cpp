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
    ListNode* swapPairs(ListNode* head) {
        ListNode *t = NULL, *origin = new ListNode(0), *prev = origin;
        origin->next = head;
        while (head != NULL && head->next != NULL) {
            t = head->next;
            prev->next = t;
            head->next = head->next->next;
            t->next = head;
            prev = head;
            head = head->next;
        }
        return origin->next;
    }
};
