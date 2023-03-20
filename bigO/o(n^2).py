
# O(n^2)
# def print_n_items(n):
    
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):     
#                 print(i, j, k)

# print_n_items(10)
            
# Drop non-dominant
def show_items(num):
    # O(n^2)
    for i in range(num):
        for j in range(num):
            print(i, j)
    # O(n)
    for k in range(num):
        print(k)
        
show_items(10)
        
            
