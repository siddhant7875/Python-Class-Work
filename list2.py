#wap to swap two numbers in a list (list of 6) 2nd element with 4th element
# Original list with six elements
my_list = [10, 20, 30, 40, 50, 60]
print("Original list:", my_list)

# Swap the 2nd element (index 1) with the 4th element (index 3)
my_list[1], my_list[3] = my_list[3], my_list[1]

# Display the result
print("List after swapping 2nd and 4th elements:", my_list)
