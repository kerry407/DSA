
# O(n)

def show_items(n):
    for i in range(n):
        print(i)
        
show_items(10)

# drop constant, O(2n) => O(n) 
def print_items(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j) 
        
print_items(10)

