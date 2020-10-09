class TwoSum {
public:
    unordered_map<long, int> map;
    /** Initialize your data structure here. */
    TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        if (map.find(number) == map.end()) map[number] = 1;
        else map[number]++;
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (auto it : map) {
            long target = value - it.first;
            if (map.count(target) > 0 && (target != it.first || map[target] > 1)) return true;
        }
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
 