class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counter;
        int maximum_count = 0;
        int maximum_groups = 0;
        int total_tasks = tasks.size();
        for (char task : tasks) {
            counter[task]++;
            if (counter[task] > maximum_count) {
                maximum_count = counter[task];
                maximum_groups = 0;
            }
            if (counter[task] == maximum_count) {
                maximum_groups++;
            }
        }

        return max((n+1)*(maximum_count-1)+maximum_groups, total_tasks);
    }
};
