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
    bool isPalindrome(ListNode* head) {
        if (head == NULL || head->next == NULL) return true;
        ListNode *slow = head;
        ListNode *fast = head;
        
        // Find middle point
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        // Reverse the latter part of the linked list
        if (fast) slow = slow->next;
        ListNode *rev = slow;
        fast = rev->next;
        rev->next = NULL;
        while (fast) {
            slow = fast->next;
            fast->next = rev;
            rev = fast;
            fast = slow;
        }

        // Check whether the 2 lists were the same => palindrome
        slow = head;
        while (rev) {
            if (rev->val == slow->val) {
                rev = rev->next;
                slow = slow->next;
            }
            else return false;
        }
        return true;
    }
};
