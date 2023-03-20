
# num1 = 11
# num2 = num1 

# print("Before update")

# print("num1:", num1)
# print("num2:", num2)

# print("After update")
# num1 = 22


# print("num1:", num1)
# print("num2:", num2)



dict1 = {
    "value": 11
}

dict2 = dict1

print("Before update")
print(f"dict1: {dict1}", f"dict2: {dict2}")

dict1.update({"length": 2})

print("After update")
print(f"dict1: {dict1}", f"dict2: {dict2}")

