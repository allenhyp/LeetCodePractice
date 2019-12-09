# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.appendLeftSubtree(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ret = self.stack.pop()
        if ret.right is not None:
            self.appendLeftSubtree(ret.right)
        
        return ret.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
    
    def appendLeftSubtree(self, root):
        cur = root
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left
        return


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
