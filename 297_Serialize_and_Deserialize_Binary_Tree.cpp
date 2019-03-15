/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
private:
    void encoder(TreeNode* root, ostringstream& out) {
        if (!root) {
            out << "# ";
            return;
        }
        out << to_string(root->val) + " ";
        encoder(root->left, out);
        encoder(root->right, out);
    }
    
    TreeNode* decoder(istringstream &in) {
        string val;
        in >> val;
        if (val == "#") return NULL;
        auto root = new TreeNode(stoi(val));
        root->left = decoder(in);
        root->right = decoder(in);
        return root;
    }
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        encoder(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in;
        in.str(data);
        return decoder(in);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
