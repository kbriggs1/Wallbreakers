class LRUCache(object):
            
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        class Cache(dict):
            def __missing__(self, key):
                return None
        class LL(object):
            def __init__(self, node=None):
                self.head = node
                self.tail = self.head
            def add(self, node):
                if self.head is None:
                    self.__init__(node)
                else:
                    self.head.prev = node
                    old_head = self.head
                    self.head = self.head.prev
                    self.head.next = old_head
                    self.head.prev = None
            def remove(self, node):
                p = node.prev
                n = node.next
                if p is not None:
                    p.next = n
                    if p.prev is None:
                        self.head = p
                    if p.next is None:
                        self.tail = p
                if n is not None:
                    n.prev = p
                    if n.prev is None:
                        self.head = n
                    if n.next is None:
                        self.tail = n
            def access(self, node):
                self.remove(node)
                self.add(node)
        self.capacity = capacity
        self.map = Cache()
        self.ll = LL()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.map[key] is not None:
            self.ll.access(self.map[key])
            return self.map[key].value
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        class Node(object):
            def __init__(self, key, value):
                self.key = key
                self.value = value
                self.prev = None
                self.next = None
        if self.map[key] is not None:
            self.ll.access(self.map[key])
            self.map[key].key = key
            self.map[key].value = value
        else:
            n = Node(key, value)
            self.ll.add(n)
            self.map[key] = n
            if len(self.map) > self.capacity:
                k = self.ll.tail.key
                self.ll.remove(self.ll.tail)
                del self.map[k]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
