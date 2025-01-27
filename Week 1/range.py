# Write a Python program to check whether a number is in a given range

num = int(input("Enter a number: "))
low = int(input("Enter the low of the range: "))
high = int(input("Enter the high of the range: "))

if low <= num <= high:
    print(num, "is in the range", low, "to", high)
else:
    print(num, "is not in the range", low, "to", high)
