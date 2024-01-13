class LRUCache {
private:
    list<pair<int, int>> items;
    unordered_map<int, list<pair<int, int>>::iterator> cache;
    int _capacity;
public:
    LRUCache(int capacity) {
        _capacity = capacity;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        items.splice(items.begin(), items, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it == cache.end()) {
            if (items.size() == _capacity) {
                cache.erase(items.back().first);
                items.pop_back();
            }
            items.push_front({key, value});
            cache[key] = items.begin();
        }
        else {
            it->second->second = value;
            items.splice(items.begin(), items, it->second);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 