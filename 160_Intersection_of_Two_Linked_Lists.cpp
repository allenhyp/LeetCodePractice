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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int countA = 0, countB = 0;
        ListNode *a = headA;
        ListNode *b = headB;
        while (a || b) {
            if (a) {
                a = a -> next;
                countA++;
            }
            if (b) {
                b = b -> next;
                countB++;
            }
        }
        int larger = max(countA, countB);
        int smaller = 0;
        ListNode* l;
        ListNode* s;
        if (larger == countA) {
            l = headA;
            s = headB;
            smaller = countB;
        }
        else {
            l = headB;
            s = headA;
            smaller = countA;
        }
        for (int i = larger - smaller; i > 0; i--) l = l -> next;
        while (l && s) {
            if (l == s) return l;
            l = l -> next;
            s = s -> next;
        }
        return NULL;
    }
};
