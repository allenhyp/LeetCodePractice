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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int iter = 1, k = lists.size();
        while (iter < k) {
            for (int j = 0; j < k - iter; j += iter * 2) {
                lists[j] = merge2List(lists[j], lists[j+iter]);
            }
            iter *= 2;
        }
        return k > 0 ? lists[0] : NULL;
    }
private:
    ListNode* merge2List(ListNode* list1, ListNode* list2) {
        ListNode* iter1 = list1;
        ListNode* iter2 = list2;
        ListNode* head = new ListNode(0);
        ListNode* point = head;
        while (iter1 && iter2) {
            if (iter1->val < iter2->val) {
                point->next = iter1;
                iter1 = iter1->next;
            }
            else {
                point->next = iter2;
                iter2 = iter2->next;
            }
            point = point->next;
        }
        if (iter1) point->next = iter1;
        else if (iter2) point->next = iter2;
        return head->next;
    }
};
