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
    vector<Interval> intervalIntersection(vector<Interval>& A, vector<Interval>& B) {
        vector<Interval> res;
        for (int i = 0, j = 0; i < A.size() && j < B.size(); ) {
            if (A[i].end < B[j].start) ++i;
            else if (B[j].end < A[i].start) ++j;
            else {
                res.push_back(Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end)));
                if (A[i].end < B[j].end) ++i;
                else ++j;
            }
        }
        return res;
    }
};
