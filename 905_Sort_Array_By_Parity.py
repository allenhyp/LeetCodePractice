class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        head, tail = 0, len(A) - 1
        curr = head
        while head < tail:
            if A[head] % 2 == 1 or A[tail] == 0:
                A[head], A[tail] = A[tail], A[head]
            while A[head] % 2 == 0 and head < tail:
                head += 1
            while A[tail] % 2 == 1 and head < tail:
                tail -= 1
        return A
