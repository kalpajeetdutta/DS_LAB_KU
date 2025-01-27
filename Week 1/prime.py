# Check if a number is a prime number

n = int(input("Enter a number: "))
is_prime = True
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
else:
    is_prime = False
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")