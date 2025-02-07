## 2) Using a while loop and input , do the following :
#- Ask the the user : "what is the  of 7 * 24 ?"
#- check if the answer is right then exit the loop and print "You answered this Question correctly"
##- if the answer is wrong, then print "Your Answer is wrong try again.." 
# and show the user the question again.

for i in range (45, 210):
    if i == 100:
        continue
    if i ==206:
        break
    print(i)

product = input("What is the product of 7 * 24? ")
ans = 168  

while True:
    # تحويل المدخل إلى عدد صحيح
    if int(product) == ans:
        print("You answered this question correctly.")
        break
    else:
        print("Your answer is wrong, try again.")
        product = input("What is the product of 7 * 24? ")  # إعادة السؤال للمستخدم

      
        





    
 
