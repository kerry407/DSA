# create new node
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
# create stack 
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
            
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            
        new_node.next = self.top
        self.top = new_node 
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None 
        if self.height == 1:
            self.top = None 
            
        temp = self.top 
        self.top = temp.next 
        temp.next = None 
        self.height -= 1
        return f"removed obj: {temp.value}"
    
my_stack = Stack(17)

my_stack.print_stack()
print("After Push")
my_stack.push(6)
my_stack.push(5)
my_stack.push(4)
my_stack.print_stack()
print(my_stack.pop())
my_stack.print_stack()




            