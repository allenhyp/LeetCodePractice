class UnionFind {
private:
    int count;
    vector<int> parent;
    vector<int> rank;
public:
    UnionFind(int N) {
        count = 0;
        for (int i = 0; i < N; ++i) {
            parent.push_back(-1);
            rank.push_back(0);
        }
    }
    
    bool isValid(int id) const {
        return parent[id] >= 0;
    }
    
    void setParent(int id) {
        parent[id] = id;
        ++count;
    }
    
    int find(int id) {
        if (parent[id] != id) parent[id] = find(parent[id]);
        return parent[id];
    }
    
    void unionIds(int a, int b) {
        int roota = find(a), rootb = find(b);
        if (roota != rootb) {
            if (rank[roota] < rank[rootb]) parent[roota] = rootb;
            else if (rank[roota] > rank[rootb]) parent[rootb] = roota;
            else {
                parent[rootb] = roota;
                ++rank[roota];
            }
            --count;
        }
    }
    
    int getCount() const {
        return count;
    }
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        UnionFind uf (m * n);
        vector<int> res;
        for (auto p : positions) {
            int x = p.first, y = p.second, id = x * n + y;
            uf.setParent(id);
            vector<int> checklist;
            if (x - 1 >= 0 && uf.isValid((x - 1) * n + y)) checklist.push_back((x - 1) * n + y);
            if (x + 1 < m && uf.isValid((x + 1) * n + y)) checklist.push_back((x + 1) * n + y);
            if (y - 1 >= 0 && uf.isValid(x * n + y - 1)) checklist.push_back(x * n + y - 1);
            if (y + 1 < n && uf.isValid(x * n + y + 1)) checklist.push_back(x * n + y + 1);
            for (auto c : checklist) uf.unionIds(c, id);
            res.push_back(uf.getCount());
        }
        return res;
    }
};
