#Assignment 2 - AncestorsQ1 - Print AncestorsGiven a Binary Tree and a key, 
# write a function that prints all the ancestors of the key in the givenbinary tree.
class Node:
 
    
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def printAncestors(root, target):
     
    if root == None:
        return False
     
    if root.data == target:
        return True
 
   
    if (printAncestors(root.left, target) or printAncestors(root.right, target)):
        print root.data,
        return True
 
    return False
 

# Test my program 
root = Node(16)
root.left = Node(9)
root.right = Node(18)
root.right.right = Node(19)
root.left.left = Node(3)
root.left.right = Node(14)
root.left.left.left = Node(1)
root.left.left.left = Node(5)
 
printAncestors(root, 5)
 
