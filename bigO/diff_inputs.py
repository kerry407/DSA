# O(a + b)
def show_items(a, b):
    # O(a)
    for i in range(a):
        print(i) 
    #O(b)   
    for j in range(b):
        print(j)
     
show_items(10, 20) 


# O(a * b)
def show_nested_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)  
            
            
show_nested_items(10,20)  
