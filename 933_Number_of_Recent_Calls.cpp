class RecentCounter {
private:
    queue<int> record;
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        record.push(t);
        while (record.front() < t - 3000)
            record.pop();
        return record.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
