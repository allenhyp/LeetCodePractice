/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        Node* iter = head;
        while (iter != NULL) {
            Node* copy = new Node(iter->val, iter->next, NULL);
            iter->next = copy;
            iter = copy->next;
        }
        iter = head;
        while (iter != NULL) {
            if (iter->random)
                iter->next->random = iter->random->next;
            iter = iter->next->next;
        }
        Node* dummy = new Node();
        Node* dup_iter = dummy;
        iter = head;
        while (iter != NULL) {
            dup_iter->next = iter->next;
            iter->next = iter->next->next;
            dup_iter = dup_iter->next;
            iter = iter->next;
        }
        return dummy->next;
    }
};
