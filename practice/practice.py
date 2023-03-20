
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node 
        self.height = 1
        
    def print_stack(self):
        temp = self.top 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        
    def insert(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node 
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None  
        if self.height == 1:
            self.top = None 
        else:
            temp = self.top
            self.top = temp.next 
            temp.next = None 
        self.height -= 1
        return True 
                        
    
    
my_stack = Stack(17)
my_stack.insert(4)
my_stack.insert(6)
my_stack.print_stack()
print("")
my_stack.pop()
my_stack.print_stack()

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1
        
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next 
            
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node 
            self.length += 1
        return True     
    
    def dequeue(self):
        if self.length == 0:
            return None 
        if self.length == 1:
            self.first = None 
            self.last = None 
        else:
            temp = self.first 
            self.first = temp.next 
            temp.next = None 
        self.length -= 1
        return True 
        
        
my_queue = Queue(17)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print_queue()
print(f"first: {my_queue.first.value}, last: {my_queue.last.value}")
print("")
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
print(f"first: {my_queue.first.value}, last: {my_queue.last.value}")



class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node 
            return True 
        else:
            temp = self.root
            while temp is not None:
                if new_node.value == temp.value:
                    return None 
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node 
                        return True
                    temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True 
                    temp = temp.right
                    
    def lookup(self, value):
        temp = self.root 
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False 

                    
                
    
my_tree = BinarySearchTree(17)
my_tree.insert(4)
my_tree.insert(19)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.lookup(16))


def check_common_items(list1: list, list2: list):
    for j in list2:
        if j in list1:
            return True   
    return False 

def check_common_items(list1: list, list2: list):
    my_dict = {}
    for i in list1:
        my_dict[i] = True 
    
    for j in list2:
        if j in my_dict:
            return True 
    return False     

list1 = [1,3,6]
list2 = [2,4,5]



print(check_common_items(list1, list2))


