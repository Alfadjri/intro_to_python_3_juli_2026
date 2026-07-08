# inisialisasi
my_list = [1,2,3,4,5]

# menampilkan list
print("===== menampilkan list =====")
print(f"List : {my_list}")
print(f"List index ke-4 : {my_list[4]}")

# CRUD
# C Create
# R Read
# U Update
# D Delete

#  A Append
my_list.append(10)
print(f"List : {my_list}")
#  U Update
my_list[0] = 20
print(f"List : {my_list}")
# Delete
del my_list[5]
print(f"List : {my_list}")
