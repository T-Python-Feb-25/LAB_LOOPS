
#Task 1
numbers= range(45,210)

for num in numbers:
    if num==100:
        continue
    elif num == 205:
        break
    print(num)


#Task 2
while int(input("what is the product of 7 * 24 ? "))!=168:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")



