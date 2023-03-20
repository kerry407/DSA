# Constructor

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
        
class LinkedList:
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
            
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
        
        
    def pop(self):
        temp = self.head
        pre = self.head
        if self.length == 0:
            return None 
        elif self.length == 1:
            self.head = None
            self.tail = None 
            self.length -= 1
        else:   
            while temp.next is not None:
                pre = temp 
                temp = temp.next 
            self.tail = pre 
            self.tail.next = None 
            self.length -= 1
            
        return f"removed obj: {temp.next}"
        
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1
        
        return True 
        
        
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None 
            self.length -= 1
        
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        return f"removed obj: {temp}"
        
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next 
        return temp
    
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True 
        return False 
    
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True
    
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None  
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        prev = self.get(index -1)
        temp = prev.next 
        prev.next = temp.next
        temp.next = None 
        self.length -= 1
        return temp
    
    
    def reverse(self):
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        before = None 
        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 
            
        return self.print_list()
        
    
my_linked_list = LinkedList(17)

# my_linked_list.append()
# my_linked_list.append(5)
# my_linked_list.append(6)
# my_linked_list.append(7)
# my_linked_list.append(8)

my_linked_list.print_list()


# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
print("After update")
print(my_linked_list.prepend(4))
print(my_linked_list.prepend(5))
print(my_linked_list.prepend(6))
my_linked_list.print_list()
print(my_linked_list.insert(4, 19))
my_linked_list.print_list()
# reversed = my_linked_list.reverse()
# print(f"head: {my_linked_list.head.value}, Tail: {my_linked_list.tail.value}")
