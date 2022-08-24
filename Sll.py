class Sll:
    def __init__(self):
        self.head=None
    def __iter__(self):  ##The __iter__() function returns an iterator for the given object (array, set, tuple, etc. or custom objects).
        node=self.head
        while node:
            yield node
            node = node.next
    def insert(self,value,location):
        newNode=Node()
        if not self.head :
            self.head=newNode
            newNode.value=value
            return
        #Insert node at beginning
        if location==0:
            
            newNode.next=self.head
            self.head=newNode
            newNode.value=value
            return
        #insertion at the end 
        elif location ==-1:
            ptr=self.head
            newNode=Node()
            while   ptr.next is not None:
                ptr=ptr.next
            ptr.next=newNode
            newNode.value=value
        else:
            newNode=Node(value)
            ct=0
            ptr=self.head
            while location==ct-1:
                ct+=1
                ptr=ptr.next
            ptr.next=newNode


class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
    
sl1=Sll()

sl1.insert(1,0)
sl1.insert(2,0)
sl1.insert(3,-1)
print([node.value for node in sl1]) 
sl2=Sll()
# sl2.insert(1,0)
# print([node.value for node in sl2]) 



