for Number in range(45,210):
    if Number == 100:
        continue
    if Number == 205:
        break
    print(Number)


while True:
    answer = int(input("What is the product of 7*24? "))
    if answer == 168:
        print("You answered this Question correctly")
        break
    else:
        print("your Answer is wrong try again")