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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        if (k == 0) return vector<ListNode*>();
        else if (k == 1) return vector<ListNode*> {root};
        vector<ListNode*> result;
        int length = 0;
        ListNode *p = root;
        while (p != NULL) {
            length++;
            p = p->next;
        }
        int s = length / k;
        int r = length % k;
        p = root;
        for (int i = 0; i < k; i++) {
            ListNode *head = p;
            if (p != NULL) {
                int j = 0;
                while (j < s - 1) {
                    p = p->next;
                    j++;
                }
                if (r > 0 && s > 0) {
                    p = p->next;
                    r--;
                }
                ListNode *t = p->next;
                p->next = NULL;
                p = t;
            }
            result.push_back(head);
        }
        return result;
    }
};
