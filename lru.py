## While explaining to the interviwer start with hashmap and arraylist or queue and tell that hashmap will contain the key and value pair and list will keep the order we will keep on adding elements at the end when we need to remove from the least used element would be the first remove it and for put traverse through the list get the position remove from it and add to the end so all the operations would be O(n) complexity, same thing would be there for singly linkedlist. The array implementation is as follow just for reference
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
    #     self.cache = []  # List of (key, value)

    # def get(self, key: int) -> int:
    #     for i, (k, v) in enumerate(self.cache):
    #         if k == key:
    #             self.cache.pop(i)  # Remove from current position
    #             self.cache.append((k, v))  # Move to end (MRU)
    #             return v
    #     return -1

    # def put(self, key: int, value: int) -> None:
    #     for i, (k, v) in enumerate(self.cache):
    #         if k == key:
    #             self.cache.pop(i)  # Remove existing key
    #             break
    #     if len(self.cache) == self.capacity:
    #         self.cache.pop(0)  # Remove LRU (first element)
    #     self.cache.append((key, value))  # Insert at end (MRU)


    ## Optimized method ##
#TC - O(1) for each operation
#Sc - O(n) that is the capacity as I have to add those in hashmap and for linkedlist as well the number would be same 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # If already exsists in map
        if key in self.dict:
            node = self.dict[key]
            self.removeNode(node)
            node.val = value
            self.addNode(node)
    
        # Capacity check
        else:
            if len(self.dict) == self.capacity:
                tailprev = self.tail.prev
                self.removeNode(tailprev)
                del self.dict[tailprev.key]
            # If doesn't exsists in map 
            node = Node(value,key)
            self.dict[key] = node
            self.addNode(node)    
      

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev    

class Node:
    next = None
    prev = None
    def __init__(self,val,key):
        self.val = val
        self.key = key


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
