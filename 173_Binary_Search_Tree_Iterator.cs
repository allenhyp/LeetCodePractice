/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class BSTIterator {
    private Stack<TreeNode> s;
    public BSTIterator(TreeNode root) {
        s = new Stack<TreeNode>();
        PushAllLefts(root);
    }
    
    /** @return the next smallest number */
    public int Next() {
        var node = s.Pop();
        var cur = node.right;
        if (cur != null) {
            PushAllLefts(cur);
        }
        return node.val;
    }
    
    /** @return whether we have a next smallest number */
    public bool HasNext() {
        return s.Count() > 0;
    }
    
    private void PushAllLefts(TreeNode node) {
        for (; node != null; node = node.left)
            s.Push(node);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */
 
