# Get user input
n = int(input("Enter a positive integer: "))

# Initialize sum variable
even_sum = 0

# Iterate through numbers from 1 to n
for num in range(1, n + 1):
    if num % 2 == 0:  # Check if the number is even
        even_sum += num

# Print the result
print(f"The sum of all even numbers between 1 and {n} is: {even_sum}")
