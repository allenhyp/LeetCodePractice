class Solution {
private:
    void merge(vector<int>& nums, int l, int m, int r) {
        int i = 0, j = 0, k = l;
        int n1 = m - l + 1, n2 = r - m;
        int L[n1], R[n2];
        for (; i < n1; i++) L[i] = nums[l + i];
        for (; j < n2; j++) R[j] = nums[m + 1 + j];
        i = 0; j = 0;
        while (i < n1 && j < n2) {
            if (L[i] > R[j]) nums[k++] = L[i++];
            else nums[k++] = R[j++];
        }
        while (i < n1) nums[k++] = L[i++];
        while (j < n2) nums[k++] = R[j++];
    }
    void mergeSort(vector<int>& nums, int l, int r) {
        if (l < r) {
            int m = l + ((r - l) / 2);
            mergeSort(nums, l, m);
            mergeSort(nums, m + 1, r);
            merge(nums, l, m, r);
        }
    }
public:
    int findKthLargest(vector<int>& nums, int k) {
        mergeSort(nums, 0, nums.size() - 1);
        return (nums[k - 1]);
    }
};

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> queue;
        for (int i = 0; i < nums.size(); i++) {
            queue.push(nums[i]);
            if (queue.size() > k)
                queue.pop();
        }
        return queue.top();
    }
};
