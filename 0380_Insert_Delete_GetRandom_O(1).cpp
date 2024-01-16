class RandomizedSet {
private:
    unordered_map<int, int> umap;
    vector<int> list;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        srand(time(NULL));
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (umap.find(val) != umap.end()) return false;
        list.push_back(val);
        umap[val] = list.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (umap.find(val) == umap.end()) return false;
        int idx = list.size() - 1;
        int temp = list[idx];
        list[umap[val]] = temp;
        umap[temp] = umap[val];
        umap.erase(val);
        list.erase(list.begin() + idx);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return list[rand() % list.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
 