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
    ListNode* partition(ListNode* head, int x) {
        ListNode* less = new ListNode();
        ListNode* greater = new ListNode();
        ListNode *curr = head, *cl = less, *cg = greater;
        
        while (curr) {
            if (curr->val < x) {
                cl->next = curr;
                cl = cl->next;
            }
            else {
                cg->next = curr;
                cg = cg->next;
            }
            
            curr = curr->next;
        }
        
        cg->next = NULL;
        cl->next = greater->next;
        return less->next;
    }
};
