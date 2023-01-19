#create a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    #insert a new node at the end of the list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    
    #remove a node from the list
    def remove(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    #insert a new node at the beginning of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #insert a new node after a given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #find the length of the list
    def length(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
    
    #find the element at a given index
    def get(self, index):
        temp = self.head
        count = 0
        while (temp):
            if count == index:
                return temp.data
            count += 1
            temp = temp.next
        assert(False)
        return 0

    #find the index of a given element
    def index(self, data):
        temp = self.head
        count = 0
        while (temp):
            if temp.data == data:
                return count
            count += 1
            temp = temp.next
        assert(False)
        return 0
    
    #reverse the list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

list2.printList() 
print('\n')
list2.reverse()
list2.printList() 

