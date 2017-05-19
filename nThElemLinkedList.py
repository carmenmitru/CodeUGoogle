"""
Implement an algorithm to find the kth to last element of a singly linked list.

The first approach is to loop through the list so we could get the lenght of the linked list ,N.
Next we can see the element K th to the last element using formula : ( length(list)- k + 1 )

Complexity :
Time complexicity: O(k)
Space complexicity: O(1)

"""
class Node():
    def __init__(self, val):
        self.next = None
        self.value = val
    
    def next(self):
        return self.next
    
    def setNext(self, nextNode):
        self.next = nextNode
        

def findElement(head, k):
    if head == None:
        return None
    
    #get the length of the list 
    currentNode = head
    num = 1  
    while currenNode.next:
        num += 1
        currentNode = currentNode.next
    
    #Special cases when 
    if num < N or N <= 0: 
        return None
        
    if N <= 0: 
        return None
    
    # get num - k + 1 node
    currentNode = head
    currentNum  = 1
    while currentNum < num - k + 1:
        currentNum += 1
        currentNode = currentNode.next
    return currentNode.value