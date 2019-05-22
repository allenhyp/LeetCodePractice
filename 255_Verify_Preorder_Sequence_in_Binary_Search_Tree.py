class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, lower = [], float('-inf')
        for p in preorder:
            if p < lower:
                return False
            while len(stack) and p > stack[-1]:
                lower = stack.pop()
            stack.append(p)
        return True
