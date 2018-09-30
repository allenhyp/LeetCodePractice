/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
    ListNode* reverseList(ListNode* curr) {
        ListNode* pre = NULL;
        ListNode* next = NULL;
        while (curr) {
            next = curr->next;
            curr->next = pre;
            pre = curr;
            curr = next;
        }
        return pre;
    }
    int checkCarry(ListNode* node) {
        if (node->val > 9) {
            node->val -= 10;
            return 1;
        }
        return 0;
    }

public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverseList(l1);
        l2 = reverseList(l2);        
        int carry = 0;
        ListNode* res = NULL;
        ListNode* pre = res;
        while (l1 || l2 || carry) {
            ListNode* node = new ListNode(0);
            if (l1 && l2) {
                node->val = l1->val + l2->val + carry--;
                carry = checkCarry(node);
                l1 = l1->next;
                l2 = l2->next;
            }
            else if (l1) {
                node->val = l1->val + carry--;
                carry = checkCarry(node);
                l1 = l1->next;
            }
            else if (l2) {
                node->val = l2->val + carry--;
                carry = checkCarry(node);
                l2 = l2->next;
            }
            else if (carry) node->val = carry--;
            
            if (res == NULL) {
                res = node;
                pre = res;
            }
            else {
                pre->next = node;
                pre = node;
            }
        }
        pre->next = NULL;
        return reverseList(res);
    }
};
