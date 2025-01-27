# Write a Python program that takes a list and returns a new list with unique elements of the first list

original_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_list = list(set(original_list))
print("Unique elements:", unique_list)