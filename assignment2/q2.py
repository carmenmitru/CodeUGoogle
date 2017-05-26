# Design an algorithm and write code to find the lowest common ancestor of two nodes in a binary tree.
#Avoid storing additional nodes in a data structure.
class Node:
 

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 


    def lca(root, n1, n2):
     
  
        if root is None:
            return None
 
        # If both n1 and n2 are smaller than root, then search in the left side
        if(root.data > n1 and root.data > n2):
            return lca(root.left, n1, n2)
 
        # If both n1 and n2 are greater than root, then search it in right side
       if(root.data < n1 and root.data < n2):
            return lca(root.right, n1, n2)
 
        return root
 

