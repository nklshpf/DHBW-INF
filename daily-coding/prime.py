def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
user_input = int(input("Enter an integer: "))

# Check if the input is a prime number
result = is_prime(user_input)

# Display the result
print(f"{user_input} is {'prime' if result else 'not prime'}.")

