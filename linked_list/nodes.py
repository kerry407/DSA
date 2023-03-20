# To present a linked lists such as: 17 --> 23 --> 3 --> 7-->None 
# where 17 is head and 7 is tail 

head = {
        "value": 17,
        "next" : {
                    "value": 23,
                    "next": {
                                "value": 3,
                                "next": {
                                            "value": 7,
                                            "next": None 
                                        }
                            }
                    }
       }
 


print(head["next"]["next"]["value"])

# If this is a linked list:
# print(my_linked_list.head.next.next.value)