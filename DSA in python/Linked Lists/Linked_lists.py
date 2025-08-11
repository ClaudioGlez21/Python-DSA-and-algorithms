# Singly Linked list

class SinglyNode:
    def __init__(self,val,next=None) -> None:
        self.val= val  
        self.next = next

    def __str__(self) -> str:
        return str(self.val)
    
head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(7)

head.next = A
A.next = B

print(head)

#traversing the linked list O(n)
curr = head

while curr:
    print(curr)
    curr = curr.next

#Search for node value - O(n)
def search(head,value):
    curr = head 
    while curr:
        if curr.val== value:
            return True
        curr = curr.next
    return False

print(search(head,4))
print(search(head,7))


# Doubly linked list


class DoublyNode:
    def __init__(self,val,next=None,prev = None) -> None:
        self.val =val
        self.next=next
        self.prev=prev
    
    def __str__(self) -> str:
        return str(self.val)
    
head = tail = DoublyNode(1) # both head and tail are pointing to the same node

# Display the elements of the doubly linked list
def display (head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("<->".join(elements))

head = DoublyNode(3)

#Insert at the beginngin of the doubly linked list O(1)
def insert_at_beginning(head,tail,val): #Basically we are gettinga new head 
    new_node = DoublyNode(val,next=head)
    head.prev = new_node
    return new_node,tail

def insert_at_end(head,tail,val):
    new_node =DoublyNode(val,prev=tail) #Point the new val, to the tail
    tail.next =new_node #Old tail to point to new node
    return head,new_node 



     


