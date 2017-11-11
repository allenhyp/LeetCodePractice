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
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL || head->next->next == NULL) return;
        ListNode *p1 = head;
        ListNode *p2 = head;

        // Find the middle point
        while (p2 && p2->next) {
            p1 = p1->next;
            p2 = p2->next->next;
        }

        // Reverse the latter part of the linked list
        ListNode *head2 = p1->next;
        p1->next = NULL;
        p2 = head2->next;
        head2->next = NULL;
        while (p2) {
            p1 = p2->next;
            p2->next = head2;
            head2 = p2;
            p2 = p1;
        }

        // Reorder the list
        p1 = head;
        p2 = head2;
        while (p2) {
            auto temp = p1->next;
            p1 = p1->next = p2;
            p2 = temp;
        }
    }
};
