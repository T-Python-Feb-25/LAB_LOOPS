# LAB_LOOPS
# 1
sequence_number=range(45,210)

for i in sequence_number:
    if i ==100:
        continue
    elif i==205:
        break
    else:
        print(f" the element is {i}")
        i+=1


# 2

X=int(input("what is the product of 7 * 24 ?"))
  
z=7*24 #168

while X != z :
    print("Your Answer is wrong try again..")
    X=int(input("what is the product of 7 * 24 ?"))
else:
    print("You answered this Question correctly")
    
 
 
 
