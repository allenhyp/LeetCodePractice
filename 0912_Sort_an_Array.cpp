// Merge Sort
class Solution {
private:
    void merge(vector<int>& nums, int low, int mid, int high) {
        vector<int> left_part (nums.begin() + low, nums.begin() + mid + 1);
        vector<int> right_part (nums.begin() + mid + 1, nums.begin() + high + 1);
        int li = 0, ri = 0, index = low;
        while (li < left_part.size() && ri < right_part.size()) {
            if (left_part[li] <= right_part[ri]) nums[index++] = left_part[li++];
            else nums[index++] = right_part[ri++];
        }

        while (li < left_part.size()) nums[index++] = left_part[li++];
        while (ri < right_part.size()) nums[index++] = right_part[ri++];
    }

    void merge_sort(vector<int>& nums, int low, int high) {
        if (low >= high) return;
        int mid = low + (high - low) / 2;
        merge_sort(nums, low, mid);
        merge_sort(nums, mid + 1, high);
        merge(nums, low, mid, high);
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        merge_sort(nums, 0, nums.size() - 1);
        return nums;
    }
};

// Quick Sort (TLE)
class Solution {
private:
    int partition(vector<int>& nums, int low, int high) {
        int pivot = nums[high];
        int cur = low - 1;
        for (int i = low; i < high; ++i) {
            if (nums[i] < pivot) swap(nums[++cur], nums[i]);
        }
        swap(nums[++cur], nums[high]);
        return cur;
    }
    void quickSort(vector<int>& nums, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(nums, low, high);
            quickSort(nums, low, pivotIndex - 1);
            quickSort(nums, pivotIndex + 1, high);
        }
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
};