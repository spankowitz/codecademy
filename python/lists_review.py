

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
print(first_names)

preferred_size = ["Small", "Large", "Medium"]
print(preferred_size)

preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True],["Ben", "Large", False],["Chani", "Medium", True],["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False
print(customer_data)

customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

customer_data_final.append(["KJ", "X-Small", True])
print(customer_data_final)
