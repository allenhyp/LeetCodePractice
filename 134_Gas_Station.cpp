class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0, subsum = INT_MAX, start = 0;
        for (int i = 0; i < gas.size(); ++i) {
            total += gas[i] - cost[i];
            if (total < subsum) {
                start = i + 1;
                subsum = total;
            }
            cout << total << ", " << subsum << endl;
        }
        return total < 0 ? -1 : start % gas.size();
    }
};
