
def split_list(a_list): # [0, 1, 2, 3, 4, 5]
    sorted_list = sorted(a_list)
    half = len(a_list) // 2  # 3
    first_half = sorted_list[:half] # 0 to 2
    second_half = sorted_list[half:]

    lookup = 5
    
    if lookup < second_half[0]:
        first_half_cut = first_half[:len(first_half)//2]
        second_half_cut = first_half[len(first_half)//2:] 
        del second_half
        
        if lookup < second_half_cut[0]:
            last_first_half_cut = first_half_cut[:len(first_half_cut)//2]
            last_second_half_cut = first_half_cut[len(first_half_cut)//2:]
        else:
            last_first_half_cut = second_half_cut[:len(second_half_cut)//2]
            last_second_half_cut = second_half_cut[len(second_half_cut)//2:]
            
        if lookup == last_first_half_cut[0]:
            print(f"lookup number found in last first half and index in original list is {a_list.index(lookup)}")
        elif lookup == last_second_half_cut[0]:
            print(f"lookup number found in last second half and index in original list is {a_list.index(lookup)}")
        else:
            print("Lookup number does not exist in list")
    else:
        first_half_cut = second_half[:len(second_half)//2]
        second_half_cut = second_half[len(second_half)//2:]        
        del first_half
        
        if lookup < second_half_cut[0]:
            last_first_half_cut = first_half_cut[:len(first_half_cut)//2]
            last_second_half_cut = first_half_cut[len(first_half_cut)//2:]
        else:
            last_first_half_cut = second_half_cut[:len(second_half_cut)//2]
            last_second_half_cut = second_half_cut[len(second_half_cut)//2:]
        
        if lookup == last_first_half_cut[0]:
            print(f"lookup number found in last first half and index in original list is {a_list.index(lookup)}")
        elif lookup == last_second_half_cut[0]:
            print(f"lookup number found in last second half and index in original list is {a_list.index(lookup)}")
        else:
            print("Lookup number does not exist in list")
        
    print(last_first_half_cut)
    print(last_second_half_cut)
    
   
    

split_list([1, 2, 3, 4, 5, 6, 7, 8])




