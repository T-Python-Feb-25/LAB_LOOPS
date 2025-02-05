#create loop for nums from 45 to 210
nums = range(45, 211) #because i want it end at 210 

#loop 
for number in nums: 
    if number == 100 :
        continue #skip num 100
    print(number)
    if number == 205: 
        break #stop at 205 
    
    