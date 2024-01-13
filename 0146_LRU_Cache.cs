public class LRUCache {
    public class ListNode {
        public int key;
        public int val;
        public ListNode next;
        public ListNode prev;
        
        public ListNode(int key, int val) {
            this.key = key;
            this.val = val;
            this.next = null;
            this.prev = null;
        }
    }
    private int Length;
    private int Capacity;
    private ListNode Head;
    private ListNode Tail;
    private Dictionary<int, ListNode> Map;
    
    public LRUCache(int capacity) {
        this.Length = 0;
        this.Capacity = capacity;
        this.Map = new Dictionary<int, ListNode>();
        this.Head = new ListNode(0, 0);
        this.Tail = new ListNode(0, 0);
        this.Head.next = this.Tail;
        this.Tail.prev = this.Head;
    }
    
    public int Get(int key) {
        int ret = -1;
        if (this.Map.ContainsKey(key)) {
            ListNode node = this.Map[key];
            ret = node.val;
            RemoveNode(node);
            AddNode(node);
        }
        return ret;
    }
    
    public void Put(int key, int value) {
        if (this.Map.ContainsKey(key)) {
            RemoveNode(this.Map[key]);
        }
        else if (this.Map.Count == this.Capacity) {
            this.Map.Remove(this.Head.next.key);
            RemoveNode(this.Head.next);
        }
        ListNode node = new ListNode(key, value);
        AddNode(node);
        this.Map[key] = node;
    }
    
    private void RemoveNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private void AddNode(ListNode node) {
        node.prev = this.Tail.prev;
        node.next = this.Tail;
        this.Tail.prev.next = node;
        this.Tail.prev = node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */