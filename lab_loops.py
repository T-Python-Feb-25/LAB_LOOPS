#task 1
for num in range(45, 211):
    if num == 100:
        continue
    if num == 205:
        break
    print(num)
# task 2
while(int(input("what is the product of 7 * 24 ?")) != (7*24) ):
    print("Your Answer is wrong try again..")
    
else:
    print("You answered this Question correctly")