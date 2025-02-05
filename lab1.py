# First Task
for i in range(45,210):
    if i == 100:
        continue
    if i == 205:
        break
    print("Number: {}".format(i))


# Second Task

result = 7 * 24
userInput = 0

while result != userInput:
    userInput = int(input("what is the product of 7 * 24 ?"))
    if (userInput != result):
        print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")

# Third Task

n = int(input("Enter a positive integer: "))
sum = 0

while n <= 0:
    n = int(input("Not valid! Enter a positive number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i  

print(f"The sum of even numbers between 1 and {n} is {sum}.")
