# Q1. Create an empty list called my_list.
my_list = []

# Q2.Append the following elements to my_list: 10, 20, 30, 40.
tempList = [10,20,30,40]
for z in tempList:
  my_list.append(z)
# ----print(my_list)

# Q3. Insert the value 15 at the second position in the list.
my_list.insert(1,15)
# ----print(my_list)

# Q4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
# ----print(my_list)

# Q5. Remove the last element from my_list.
del my_list[-1]
# ----print(my_list)

# Q6. Sort my_list in ascending order.
my_list.sort()
# ----print(my_list)

# Q7. Find and print the index of the value 30 in my_list.
print(my_list.index(30))