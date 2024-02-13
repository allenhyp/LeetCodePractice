class TrieNode {
public:
    bool isEOW;
    TrieNode* next[26];
    TrieNode() {
        isEOW = false;
        memset(next, NULL, sizeof(next));
    }
};

class WordDictionary {
private:
    TrieNode* root = new TrieNode();
    bool search(const char* word, TrieNode* node) {
        for (int i = 0; word[i] && node; i++) {
            if (word[i] != '.') {
                node = node->next[word[i] - 'a'];
            } else {
                TrieNode* tmp = node;
                for (int j = 0; j < 26; j++) {
                    node = tmp->next[j];
                    if (search(word+i+1, node)) return true;
                }
            }
        }
        return node && node->isEOW;
    }
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->next[c - 'a']) {
                node->next[c - 'a'] = new TrieNode();
            }
            node = node->next[c - 'a'];
        }
        node->isEOW = true;
    }
    
    bool search(string word) {
        return search(word.c_str(), root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
