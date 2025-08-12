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
        node = stack.pop() # we process the node that is in the top of the stack
        print(node)
        if node.right:stack.append(node.right)
        if node.left: stack.append(node.left)
        # we do right then left so that the left node ends on top of the stack, 
        # because we need to go down the left side first

pre_order_iterative(A)

# Level order traversla (BFS) Time complexity: O(n) space: O(n)

from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
level_order(A)


#Check if a value exists (DFS) Time: O(n)
def search (node,target):
    if not node:
        return False # we did not find the target
    if node.val  == target:
        return True
    return search(node.left,target) or search(node.right,target)

search(A,4)
