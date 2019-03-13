/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return recursive(grid, 0, 0, grid.size());
    }
private:
    Node* recursive(vector<vector<int>>& g, int x, int y, int length) {
        if (length == 1) return new Node(g[x][y] == 1, true, NULL, NULL, NULL, NULL);
        int half = length / 2;
        Node* tl = recursive(g, x, y, half);
        Node* tr = recursive(g, x, y + half, half);
        Node* bl = recursive(g, x + half, y, half);
        Node* br = recursive(g, x + half, y + half, half);
        if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf && 
            ((tl->val && tr->val && bl->val && br->val) ||
             !(tl->val || tr->val || bl->val || br->val))) {
            bool val = tl->val;
            tl = NULL; delete tl;
            tr = NULL; delete tr;
            bl = NULL; delete bl;
            br = NULL; delete br;
            return new Node(val, true, NULL, NULL, NULL, NULL);
        }
        return new Node(true, false, tl, tr, bl, br);
    }
};
