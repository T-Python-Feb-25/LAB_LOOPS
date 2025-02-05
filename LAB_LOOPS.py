# 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print
# the elements. Skip the number 100 and break the loop at 205
for num in range(45,210):
    #to skip the number 100
    if num != 100:
        print (num)
    #to break the loop when the number 205 is reached
    if num ==205:
        break

'''
## 2) Using a while loop and input , do the following :
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
'''
#initilaizing the While loop
while True:
    #asking the User to input a number
    Calculate = int(input("what is the product of 7 * 24 ? Please provide the answer?"))
    #Check the answers
    if Calculate == 168:
        print("You answered this Question correctly")
        exit()
    else:
        print ("Your Answer is wrong try again..")

'''
this is the LAB_LOOPS
Feb5, 2025
By Mohammed Albushaier
'''
