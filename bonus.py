# Prompt the user for a positive integer
n = int(input("Enter a positive integer: "))

# Initialize the sum to 0
even_sum = 0

# Loop through numbers from 1 to n (inclusive)
for num in range(1, n + 1):
    if num % 2 == 0:  # Check if the number is even
        even_sum += num  # Add the even number to the sum

# Print the result
print(f"The sum of even numbers between 1 and {n} is {even_sum}.")