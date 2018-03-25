class Solution {
public:
    vector<string> dic = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    struct treeNode {
        struct treeNode *left;
        struct treeNode *right;
        int val = 0;
    };
    void helper(struct treeNode *node, int &cnt) {
        if (node->left != NULL) helper(node->left, cnt);
        if (node->right != NULL) helper(node->right, cnt);
        if (node->left == NULL && node->right == NULL || node->val == 1) cnt++;
    }
    int uniqueMorseRepresentations(vector<string>& words) {
        struct treeNode *root = new treeNode();
        int size = words.size();
        if (size < 1) return 0;
        for (int i = 0; i < size; i++) {
            struct treeNode *r = root;
            for (int j = 0; j < words[i].size(); j++) {
                string t = dic[words[i][j] - 'a'];
                for (int k = 0; k < t.size(); k++) {
                    if (t[k] == '.') {
                        if (r->left == NULL)
                            r->left = new treeNode();
                        r = r->left;
                    }
                    else {
                        if (r->right == NULL)
                            r->right = new treeNode();
                        r = r->right;
                    }
                }
            }
            r->val = 1;
        }
        struct treeNode *r = root;
        int count = 0;
        helper(r, count);
        return count;
    }
};
