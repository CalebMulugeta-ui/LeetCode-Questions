class Node:
    def __init__(self, key,val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.map = {} #map from key to the node that holes that keys pair

        #left helps find least used, right is most used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left


    #remove node from left list
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    #insert node from right of the list    
    def insert(self,node):
        right = self.right
        left = right.prev

        left.next, right.prev = node, node
        node.next, node.prev = right, left

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key,value)
        self.insert(self.map[key])

        if (len(self.map)) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)