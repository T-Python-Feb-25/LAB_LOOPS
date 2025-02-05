#/////////////task1/////////////

for num in range(45, 211):  
    if num == 100:
        continue  
    if num == 205:
        break  
    print(num)



#//////////////task2////////////////
print("task2_while loop")

correct_answer = 7 * 24  


while True:
    user_answer = int(input("What is the product of 7 * 24?"))  

    if user_answer == correct_answer:
        print("You answered this Question correctly!")
        break  
    else:
        print("Your Answer is wrong. Try again..")