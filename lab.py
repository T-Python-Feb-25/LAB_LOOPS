# Task 1: Using range() with a for loop
for number in range(45, 210):
    if number == 100:
        continue  # Skip 100
    if number == 205:
        break  # Exit the loop at 205
    print(number)
    
    
# Task 2: Using while loop and input for question
while True:
    answer = input("What is the product of 7 * 24? ")

    # Check if the answer is correct
    if answer == '168':
        print("You answered this question correctly!")
        break  # Exit the loop when the answer is correct
    else:
        print("Your answer is wrong. Try again...")

