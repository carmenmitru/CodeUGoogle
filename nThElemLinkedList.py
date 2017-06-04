"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""
class Node(object):
    # Function to initialize the node object
    def __init__(self, data=None, next_node=None):
        self.data = data  # Assign data
        self.next_node = next_node  # Initialize 
                          # next as null
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    # Function to initialize the Linked 
    # List object
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        # 1 & 2: Allocate the Node &
        #Put in the data
        new_node = Node(data)
        # 3. Make next of new Node as head
        new_node.set_next(self.head)
        # 4. Move the head to point to new Node 
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

      
    def kth_to_last_node(self,k):
        if k < 1:
            raise ValueError("Impossible to find less than first to last node")
        current = self.head
        count = 0
        s = self.size()
        
        if k > s:
            raise ValueError("K is larger than the length of the linked list")
   
        while current is not None and count < s - k:
            count += 1
            current = current.get_next()
        print current.get_data()
            
       
         
         

temp = LinkedList()
temp.insert(3)
temp.insert(4)
temp.insert(5)
temp.insert(6)
temp.kth_to_last_node(1)
