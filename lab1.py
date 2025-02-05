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