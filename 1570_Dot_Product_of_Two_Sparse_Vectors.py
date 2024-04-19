class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.hm[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        hm1, hm2 = self.hm, vec.hm
        if len(hm1.keys()) > len(hm2.keys()):
            hm1, hm2 = hm2, hm1

        for k, v in hm1.items():
            if k in hm2:
                ret += v * hm2[k]
        return ret
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
