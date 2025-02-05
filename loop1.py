
numbers = [i for i in range(45, 211) if i != 100]  


for i in numbers:
    if i == 205:                                #سلسلة من الارقام وضعناها بين range(45,211)                                                
        break                                                       #ثم يتحقق يعد كذا ان الرقم ما يكون 100
    print(i)                                                           
        


while True:
    answer = int(input("What is the product of 7 * 24? "))  
    if answer == 168:  
        print("You answered this Question correctly")
        break  
    else:     
        print("Your Answer is wrong, try again...")
