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
    ListNode* mergeList(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0), *p = head;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                p->next = l1;
                l1 = l1->next;
            }
            else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if (l1 != NULL)
            p->next = l1;
        if (l2 != NULL)
            p->next = l2;
        return head->next;
    }
    ListNode* sortList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *prev = NULL, *slow = head, *fast = head;
        while (fast != NULL && fast->next != NULL) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = NULL;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        return mergeList(l1, l2);
    }
};
