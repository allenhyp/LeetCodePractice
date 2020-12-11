class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if (n < 3 || arr[0] >= arr[1]) return false;
        bool peak = false;
        for (int i = 1; i < n; ++i) {
            if (peak && arr[i] > arr[i - 1] || arr[i] == arr[i - 1]) return false;
            peak = arr[i] < arr[i - 1];
        }
        return peak;
    }
};
