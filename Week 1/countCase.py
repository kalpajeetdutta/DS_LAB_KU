# Calculate the number of upper case letters and lower case letters in a string

string = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)