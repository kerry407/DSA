
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.value = value 
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 
        
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
            self.tail.next = None 
        self.length += 1
        return True 
    
    def pop(self):
        if self.length == 0:
            return None 
        
        temp = self.tail
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else:
            self.tail = temp.prev
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head 
            self.head = new_node
        self.length += 1
        return True  
    
    def pop_first(self):
        if self.length == 0:
            return None 
        
        temp = self.head
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
            self.head.prev = None  
            temp.next = None    
        self.length -= 1
        return temp
    
    def get(self, index):
        """
        We will optimize this function by checking the 
        length of the list and checking the halves to see 
        where to start looping from.
        """
        if index < 0 or index >= self.length:
            return None 
        if index < self.length/2:
            temp = self.head 
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail 
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
                
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False  
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False 
        elif index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
    
        after = self.get(index)
        before = after.prev 
        new_node.next = before.next 
        new_node.prev = after.prev 
        before.next = new_node
        after.prev = new_node 
        self.length += 1  
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False 
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        after = temp.next 
        before = temp.prev 
        before.next = after 
        after.prev = before 
        temp.next = None 
        temp.prev = None 
        self.length -= 1
        return temp.prev
        
        
        
            
            
my_linked_list = DoublyLinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print_list()
print(f"length: {my_linked_list.length}")
print(my_linked_list.remove(1))
my_linked_list.print_list()
print(f"length: {my_linked_list.length}")
print(f"head: {my_linked_list.head.value}, tail: {my_linked_list.tail.value}")





    