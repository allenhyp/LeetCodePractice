class MinStack {
private:
    struct element {
        long value;
        long min;
    };

    stack<element> realStack;

public:
    /** initialize your data structure here. */
    // MinStack() {
    //      realStack = new stack<element>;
    // }
    
    void push(int x) {
        element e;
        e.value = x;
        if (!realStack.empty()) {
            if (realStack.top().min >= x) e.min = x;
            else e.min = realStack.top().min;
        }
        else {
            e.min = x;
        }
        realStack.push(e);
    }
    
    void pop() {
        realStack.pop();
    }
    
    int top() {
        return realStack.top().value;
    }
    
    int getMin() {
        return realStack.top().min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
