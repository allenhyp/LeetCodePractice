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
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast) {
            if (fast->next) {
                slow = slow->next;
                if (fast->next->next) {
                    fast = fast->next->next;
                }
                else break;
            }
            else break;
        }
        return slow;
    }
};
