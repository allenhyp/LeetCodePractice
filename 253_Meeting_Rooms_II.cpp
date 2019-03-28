/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> starts, ends;
        for (auto interval : intervals) {
            starts.push_back(interval.start);
            ends.push_back(interval.end);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        int need = 0;
        for (int i = 0, cur = 0; i < starts.size(); ++i) {
            if (starts[i] < ends[cur])
                ++need;
            else
                ++cur;
        }
        return need;
    }
};

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [] (Interval a, Interval b) {return a.start < b.start;});
        priority_queue<int, vector<int>, greater<int>> needs;
        for (auto interval : intervals) {
            if (needs.empty() || interval.start < needs.top())
                needs.push(interval.end);
            else {
                needs.pop();
                needs.push(interval.end);
            }
        }
        return needs.size();
    }
};
