/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Codec {
private:
    void encode(Node* root, string& s) {
        if (!root) return;
        s += " " + to_string(root->val) + " " + to_string(root->children.size());
        for (auto it : root->children) encode(it, s);
    }
    
    Node* decode(stringstream& ss) {
        ss.peek();
        if (ss.eof()) return NULL;
        int size;
        auto root = new Node();
        ss >> root->val >> size;
        for (int i = 0; i < size; ++i)
            root->children.push_back(decode(ss));
        return root;
    }
public:

    // Encodes a tree to a single string.
    string serialize(Node* root) {
        string s = "";
        encode(root, s);
        return s;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        stringstream ss;
        ss.str(data);
        return decode(ss);
    }
    
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
