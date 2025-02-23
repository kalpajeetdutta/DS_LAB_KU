# Calculate the sum of the digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
