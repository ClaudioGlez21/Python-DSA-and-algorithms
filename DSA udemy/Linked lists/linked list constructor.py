class Node:
    def __init__(self,value) -> None: #since all the methods of the linked list need a new node, we create a new class that creates the new node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value): #Create a node and initialize the linked list
        new_node = Node(value)
        self.head= new_node
        self.tail = new_node
        self.length=1

    def append(self,value):#create a new node and add the node to the end
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next =new_node
            self.tail = new_node       # Actualizar la cola a ser el nuevo nodo
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head

        while(temp.next):# meintras siga habiendo algo en el siguiente nodo, seguria hasta el ultimo element
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp

    def prepend(self,value): #create a new node and add Node to the beginning
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head=new_node
            new_node.next=temp
        self.length+=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            sec_element = self.head.next
            self.head = sec_element
            temp.next=None
            self.length-=1
            



    def insert(self,value): #Create a node and insert it at an specific location
        pass
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

mylinkedlist = LinkedList(7)
mylinkedlist.append(2)
print(mylinkedlist.print_list())

