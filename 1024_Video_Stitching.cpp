class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int T) {
        vector<int> max_range (T + 1, 0);
        for (auto clip : clips) {
            if (clip[0] < T + 1) {
                max_range[clip[0]] = max(max_range[clip[0]],
                                         min(clip[1] - clip[0], T - clip[0]));
            }
        }
        int start = 0, end = 0, step = 0;
        while (end < T) {
            ++step;
            int tmp = end;
            for (int i = start; i <= tmp; ++i) {
                end = max(end, i + max_range[i]);
            }
            start = tmp;
            if (start == end) return -1;
        }
        return step;
    }
};
