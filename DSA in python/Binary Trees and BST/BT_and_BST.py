class TreeNode:
    def __init__(self,val,left=None, right = None):
        self.val =val
        self.left = left
        self.right=right

    def __str__(self):
        return str(self.val)

A = TreeNode(1)    
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)

A.left=B
A.right =C
B.left=D
B.right = E
C.left=F

# Recursive Pre order Traversla (dfs) time complexity: O(n)
def pre_order(node): #If the node is None
    if not node:
        return 
    
    print(node) #this would be the "process step"
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)


# Recursive In order Traversla (dfs) time complexity: O(n)
def pre_order(node): #If the node is None
    if not node:
        return 
    
    pre_order(node.left)
    print(node) #this would be the "process step"
    pre_order(node.right)


#Iterative pre order Traversal (DFS) Time complexity: O(n)
    def pre_order_iterative(node):
        stack = [node] #Initialize with the root node
        while stack: #while we have something in the stack
            node = stk.pop() # we process the node that is in the top of the stack
