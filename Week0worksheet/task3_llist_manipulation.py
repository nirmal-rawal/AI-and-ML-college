# 1. Extract Every Other Element
lst = [1, 2, 3, 4, 5, 6]
result = lst[::2]  # Extract every other element starting from the first
print(result) 
# Output: [1, 3, 5]


# 2. Slice a Sublist
lst = [1, 2, 3, 4, 5, 6]
start = 2
end = 4
result = lst[start:end+1]  # Slice from start to end (inclusive)
print(result) 
# Output: [3, 4, 5]


#Reverse a List Using Slicing
lst = [1, 2, 3, 4, 5]
result = lst[::-1]  # Reverse the list using slicing
print(result)  

# Output: [5, 4, 3, 2, 1]


# 4. Remove the First and Last Elements
lst = [1, 2, 3, 4, 5]
result = lst[1:-1]  # Remove the first and last elements
print(result)  

# Output: [2, 3, 4]



# 5. Get the First n Elements
lst = [1, 2, 3, 4, 5]
n = 3
result = lst[:n]  # Get the first n elements
print(result)  

# Output: [1, 2, 3]\



# 6. Extract Elements from the End
lst = [1, 2, 3, 4, 5]
n = 2
result = lst[-n:]  # Get the last n elements
print(result)  

# Output: [4, 5]

# 6. Extract Elements from the End

lst = [1, 2, 3, 4, 5]
n = 2
result = lst[-n:]  # Get the last n elements
print(result)  

# Output: [4, 5]


# 7. Extract Elements in Reverse Order
lst = [1, 2, 3, 4, 5, 6]
result = lst[-2::-2]  # Extract every second element starting from the second-to-last
print(result)  

# Output: [5, 3, 1]



# 4.3 Exercise on Nested List
# 1. Flatten a Nested List

nested_lst = [[1, 2], [3, 4], [5]]
flat_list = [item for sublist in nested_lst for item in sublist]  # Flatten the list
print(flat_list)  
# Output: [1, 2, 3, 4, 5]

# 2. Accessing Nested List Elements
nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
indices = [1, 2]
result = nested_lst[indices[0]][indices[1]]  # Access the element at the given indices
print(result) 
 # Output: 6

#  3. Sum of All Elements in a Nested List
nested_lst = [[1, 2], [3, [4, 5]], 6]
# Flatten the list first
flat_list = [item for sublist in nested_lst for item in (sublist if isinstance(sublist, list) else [sublist])]
total = sum(flat_list)  # Sum all elements
print(total)  
# Output: 21

# 4. Remove Specific Element from a Nested List
nested_lst = [[1, 2], [3, 2], [4, 5]]
elem = 2
# Remove all occurrences of `elem`
result = [[item for item in sublist if item != elem] for sublist in nested_lst]
print(result)  
# Output: [[1], [3], [4, 5]]


# 5. Find the Maximum Element in a Nested List
nested_lst = [[1, 2], [3, [4, 5]], 6]
# Flatten the list first
flat_list = [item for sublist in nested_lst for item in (sublist if isinstance(sublist, list) else [sublist])]
max_val = max(flat_list)  # Find the maximum element
print(max_val) 
 # Output: 6


# 6. Count Occurrences of an Element in a Nested List
nested_lst = [[1, 2], [2, 3], [2, 4]]
elem = 2
# Flatten the list first
flat_list = [item for sublist in nested_lst for item in sublist]
count = flat_list.count(elem)  # Count occurrences of `elem`
print(count) 
 # Output: 3

#  7. Flatten a List of Lists of Lists
deep_nested_lst = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# Flatten the deeply nested list
flat_list = [item for sublist in deep_nested_lst for subsublist in sublist for item in subsublist]
print(flat_list)  

# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 8. Nested List Average
nested_lst = [[1, 2], [3, 4], [5, 6]]
# Flatten the list first
flat_list = [item for sublist in nested_lst for item in sublist]
average = sum(flat_list) / len(flat_list)  # Calculate the average
print(average)  
# Output: 3.5