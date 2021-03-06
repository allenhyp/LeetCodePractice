class Logger {
private:
    unordered_map<string, int> dic;
public:
    /** Initialize your data structure here. */
    Logger() {
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        auto it = dic.find(message);
        if (it == dic.end()) {
            dic.insert({message, timestamp});
            return true;
        }
        else {
            if (timestamp >= it->second + 10) {
                it->second = timestamp;
                return true;
            }
            else return false;
        }
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */
