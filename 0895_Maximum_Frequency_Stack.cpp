class FreqStack {
public:
    unordered_map<int, int> freqs;
    unordered_map<int, stack<int>> stacks;
    int maj = 0;
    FreqStack() {
        
    }
    
    void push(int val) {
        freqs[val]++;
        maj = max(maj, freqs[val]);
        stacks[freqs[val]].push(val);
    }
    
    int pop() {
        int ret = stacks[maj].top(); stacks[maj].pop();
        freqs[ret]--;
        if (stacks[maj].size() == 0) maj--;
        return ret;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
 